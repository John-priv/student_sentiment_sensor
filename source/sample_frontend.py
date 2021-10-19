import csv
import os
import sys
import prompts
import backendIO
from datetime import datetime
import time
import json

def main():

    latest_sent_time = "00000000000000000001"
    latest_received_time = "00000000000000000000"

    while True:
        while latest_received_time < latest_sent_time:
            filenames = os.listdir("./../data/question_messages")
            filetimes = [s.split(".")[0] for s in filenames if s.split(".")[1] == 'json']
            latest_received_time = max(filetimes)
            time.sleep(0.05)

        read_file = open("./../data/question_messages/" + latest_received_time + ".json", "r")
        question_json_string = read_file.read()
        read_file.close()

        print(question_json_string)
        print("Note: enter response ID, not index within displayed list")

        question_data = json.loads(question_json_string)
        options = question_data["Responses"]

        selection = input('')
        response_text = options[str(selection).encode('UTF-8')]

        latest_sent_time = datetime.now().strftime("%Y%m%d%H%M%S%f")

        json_response = json.dumps({"Question": "Sample text", "Selected_Response": {selection: response_text}}, sort_keys=True, indent=4)

        write_file = open("./../data/response_messages/" + latest_received_time + ".json", "w")
        write_file.write(json_response)
        write_file.close()

        print(json_response)


if __name__ == "__main__":
    main()
