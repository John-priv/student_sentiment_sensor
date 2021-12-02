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
    info_listings = {key: {'Text': ilp_dict[key].get_text(), 'Link': ilp_dict[key].get_info_link()}
                     for key in sp.get_info_listing_ids()}
    return json.dumps({"Prompt type": "Solution", "Text": solution_text, "Info Listings": info_listings})


def fromJSON(response_json, qp_dict):
    # TODO - discuss what this function should return
    json_dict = json.loads(response_json)
    question_id = list(json_dict["selectedResponse"].keys())[0]
    if question_id in qp_dict.keys():
        return question_id, qp_dict[question_id]
    elif question_id in ['emailTrue', 'emailFalse']:
        return question_id, json_dict["selectedResponse"][question_id]


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


def store_conversation(convo, time):
    write_text = json.dumps(convo, indent=4)
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/conversations/" + time + ".json"))
    write_file = open(file_path, "w")
    write_file.write(write_text)
    write_file.close()


def store_interaction(convo, emotion, u_id):
    '''
    Stores interaction as a newline separated path of [question_id, question_text, response_id, response_text]
        - NOTE: I realize that I accidentally made a worse version of a csv. Keeping for now
        - Check the first element for line type:
            "Question":   [question_id, question_text, response_id, response_text]
            "Solution":   [solution_id, solution_text, emotion_approx]
            "Emotion_CV": 'emotion'     # The detecte emotion
    '''
    # write_text = json.dumps(convo, indent=4)
    write_text = ''
    for line in convo:
        for element in line:
            write_text = write_text + (str(element)) + '|'  # separate elements by comma
        write_text = write_text[:-1] + '\n'                 # trim off trailing comma, add newline
    write_text = write_text + 'Emotion_CV|' + emotion       # end file with emotion
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/stored_user_data/" + u_id + ".dat"))
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
