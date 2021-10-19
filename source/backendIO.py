import prompts
import json
import os
import time

def toJSON(qp, rp_dict):
    question_text = qp.get_text()
    responses = {key: rp_dict[key].get_text() for key in qp.get_response_ids()}
    return json.dumps({"Question": question_text , "Responses" : responses}, sort_keys=True, indent=4)


#TODO - discuss what this function should return
def fromJSON(response_json, qp_dict):
    json_dict = json.loads(response_json)
    question_id = list(json_dict["Selected_Response"].keys())[0]
    return qp_dict[question_id]


def send_to_frontend(qp, rp_dict, time):
    write_text = toJSON(qp, rp_dict)
    write_file = open("./../data/question_messages/" + time + ".json", "w")
    write_file.write(write_text)
    write_file.close()


def read_from_frontend(old_time_string, rp_dict):
    latest_time_string = "00000000000000000000"
    while latest_time_string < old_time_string:
        filenames = os.listdir("./../data/response_messages")
        filetimes = [s.split(".")[0] for s in filenames if s.split(".")[1] == 'json']
        if len(filetimes) > 0:
            latest_time_string = max(filetimes)
        time.sleep(0.05)
    read_file = open("./../data/response_messages/" + latest_time_string + ".json", "r")
    response_json_string = read_file.read()
    read_file.close()
    return fromJSON(response_json_string, rp_dict)
