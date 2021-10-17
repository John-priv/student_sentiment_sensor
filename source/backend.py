import csv
import os
import sys
import prompts


def load_spreadsheet_old(spreadsheet, prompt_type):
    '''
    OLD FUNCTION (Clean up/staged for removal by 10/29/2021 if not reused)
    DOES NOT USE CSV LIBRARY. This leads to issues with commas in quotes not being rendered properly
    Inputs:
        spreadsheet (string): Name of csv file to load in Student_Sentiment_Sensor/data/
        prompt_type (string): Options are
            "question" for question_prompt
            "response" for response_prompt
    Output:
        prompt_dict (dict):
            - Dictionary of prompts; follows format prompt_dict[prompt_id] = prompts.prompt_type(text, ids)
    '''
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), spreadsheet))
    opened_file = open(file_path, 'r').read()
    prompt_dict = {}
    split_spreadsheet = opened_file.split('\n')
    for line in range(1, len(split_spreadsheet)):
        try:
            data = split_spreadsheet[line].split(',')
            prompt_id = data[0]
            text = data[1]
            if prompt_type == 'question':
                response_ids = data[2:]
                prompt_dict[prompt_id] = prompts.question_prompt(text, response_ids)
            if prompt_type == 'response':
                question_id = data[2]
                prompt_dict[prompt_id] = prompts.response_prompt(text, question_id)
        except Exception as e:
            print('Error in load_spreadsheet: {} --> {}'.format(split_spreadsheet[line], e))
    return prompt_dict


def load_spreadsheet(spreadsheet, prompt_type):
    '''
    Inputs:
        spreadsheet (string): Name of csv file to load in Student_Sentiment_Sensor/data/
        prompt_type (string): Options are
            "question" for question_prompt
            "response" for response_prompt
    Output:
        prompt_dict (dict):
            - Dictionary of prompts; follows format prompt_dict[prompt_id] = prompts.prompt_type(text, ids)
    '''
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), spreadsheet))
    prompt_dict = {}
    with open(file_path) as opened_file:
        csv_file = csv.reader(opened_file)
        next(csv_file)  # Skips header line
        for row in csv_file:
            try:
                prompt_id = row[0]
                text = row[1]
                if prompt_type == 'question':
                    response_ids = row[2:]
                    prompt_dict[prompt_id] = prompts.question_prompt(text, response_ids)
                if prompt_type == 'response':
                    question_id = row[2]
                    prompt_dict[prompt_id] = prompts.response_prompt(text, question_id)
            except Exception as e:
                print('Error in load_spreadsheet: {} --> {}'.format(row, e))
    return prompt_dict


def get_response_texts(response_id_list, response_prompts_dict):
    response_texts = []
    for response_id in response_id_list:
        response_texts.append(response_prompts_dict[response_id].get_text())
    return response_texts


def main():
    '''
    ARGS: backend.py QUESTION_PROMPT_NAME RESPONSE_PROMPT_NAME
        QUESTION_PROMPT_NAME and RESPONSE_PROMPT_NAME are optional args to configure the execution
    '''
    question_prompt_filename = 'Test_Tree_Question_Prompts.csv'
    response_prompt_filename = 'Test_Tree_Response_Prompts.csv'

    if len(sys.argv) >= 3:
        question_prompt_filename = sys.argv[1]
        response_prompt_filename = sys.argv[2]

    question_prompts = load_spreadsheet('../data/' + question_prompt_filename, 'question')  # dict
    response_prompts = load_spreadsheet('../data/' + response_prompt_filename, 'response')  # dict

    prompt_id = '0'
    question_prompts[prompt_id].get_response_ids()

    while True:
        open_prompt = question_prompts[prompt_id]
        response_id_list = open_prompt.get_response_ids()
        print(open_prompt.get_text())
        for response in response_id_list:
            if response in response_prompts.keys():
                print('{}: {}'.format(response_prompts[response].get_text(), response))
        print('_____________________________')

        selection = input('')
        response_id = open_prompt.get_response_ids()[int(selection)]
        response = response_prompts[response_id]
        prompt_id = response.get_question_id()
        print(prompt_id)
        if prompt_id == '0':
            do_end = input('Enter anything to exit')
            if do_end != '':
                print('')
                break


if __name__ == "__main__":
    main()
