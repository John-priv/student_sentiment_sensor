import prompts
import json
import os
import time

def questionToJSON(qp, rp_dict):
    question_text = qp.get_text()
    responses = {key: rp_dict[key].get_text() for key in qp.get_response_ids()}
    return json.dumps({"Prompt type": "Question", "Text": question_text, "Responses": responses}, sort_keys=True, indent=4)

def solutionToJSON(sp, ilp_dict):
    solution_text = sp.get_text()
    info_listings = {key: {'Text': ilp_dict[key].get_text(), 'Link': ilp_dict[key].get_info_link()} for key in sp.get_info_listing_ids()}
    return json.dumps({"Prompt type": "Solution", "Text": solution_text, "Info Listings": info_listings})

#TODO - discuss what this function should return
def fromJSON(response_json, qp_dict):
    json_dict = json.loads(response_json)
    question_id = list(json_dict["selectedResponse"].keys())[0]
    return qp_dict[question_id]


def send_question_to_frontend(qp, rp_dict, time):
    write_text = questionToJSON(qp, rp_dict)
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/question_messages/" + time + ".json"))
    write_file = open(file_path, "w")
    write_file.write(write_text)
    write_file.close()


def send_solution_to_frontend(qp, ilp_dict, time):
    write_text = solutionToJSON(qp, ilp_dict)
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/question_messages/" + time + ".json"))
    write_file = open(file_path, "w")
    write_file.write(write_text)
    write_file.close()


def read_from_frontend(old_time_string, rp_dict):
    latest_time_string = "00000000000000000000"
    while latest_time_string < old_time_string:
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/response_messages"))
        filenames = os.listdir(file_path)
        filetimes = [s.split(".")[0] for s in filenames if s.split(".")[1] == 'json']
        if len(filetimes) > 0:
            latest_time_string = max(filetimes)
        time.sleep(0.05)
    read_file = open(os.path.join(file_path, latest_time_string + ".json"), "r")
    response_json_string = read_file.read()
    read_file.close()
    return fromJSON(response_json_string, rp_dict)
