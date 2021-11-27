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
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/question_messages"))
            filenames = os.listdir(file_path)
            filetimes = [s.split(".")[0] for s in filenames if s.split(".")[1] == 'json']
            latest_received_time = max(filetimes)
            time.sleep(0.05)

        read_file = open(os.path.join(file_path, latest_received_time + ".json"), "r")
        question_json_string = read_file.read()
        read_file.close()

        print(question_json_string)
        print("Note: enter response ID, not index within displayed list")

        question_data = json.loads(question_json_string)
        if question_data["Prompt type"] == "Question":
            options = question_data["Responses"]

            selection = input('')
            response_text = options[str(selection)]

            json_response = json.dumps({"Question": "Sample text", "Selected_Response": {selection: response_text}}, sort_keys=True, indent=4)

        else:
            json_response = json.dumps({"Question": "Sample text", "Selected_Response": {10: "Back to beginning"}}, sort_keys=True, indent=4)

        # Truncate time down to the centisecond
        latest_sent_time = datetime.now().strftime("%Y%m%d%H%M%S%f")[0:-4]
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/response_messages"))

        write_file = open(os.path.join(file_path, latest_sent_time + ".json"), "w")
        write_file.write(json_response)
        write_file.close()

        print(json_response)

if __name__ == "__main__":
    main()
