import csv
import os
import sys
import prompts
import backendIO
import email_helper
from datetime import datetime


def load_spreadsheet(spreadsheet, prompt_type):
    '''
    Loads a spreadsheet (CSV file), trims the header line, and returns a dict of prompt objects
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
    with open(file_path, 'r', encoding='utf-8') as opened_file:
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
                if prompt_type == 'solution':
                    info_listing_ids = row[2:]
                    prompt_dict[prompt_id] = prompts.solutions_prompt(text, info_listing_ids)
                if prompt_type == 'info_listing':
                    link = row[2]
                    prompt_dict[prompt_id] = prompts.info_listing_prompt(text, link)
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
    question_prompt_filename = 'decision_tree/question_prompts.csv'
    response_prompt_filename = 'decision_tree/response_prompts.csv'
    solution_prompt_filename = 'decision_tree/solution_prompts.csv'
    info_listing_prompt_filename = 'decision_tree/info_listing_prompts.csv'

    if len(sys.argv) >= 3:
        question_prompt_filename = sys.argv[1]
        response_prompt_filename = sys.argv[2]

    question_prompts = load_spreadsheet('../data/' + question_prompt_filename, 'question')  # dict
    response_prompts = load_spreadsheet('../data/' + response_prompt_filename, 'response')  # dict
    solution_prompts = load_spreadsheet('../data/' + solution_prompt_filename, 'solution')
    info_listing_prompts = load_spreadsheet('../data/' + info_listing_prompt_filename, 'info_listing')

    prompt_id = '10'

    conversation = []

    conversation.append(('Emotion', 'Null'))

    while True:
        if prompt_id in question_prompts.keys():
            open_prompt = question_prompts[prompt_id]

            # Truncate time down to the centisecond
            time = datetime.now().strftime("%Y%m%d%H%M%S%f")[0:-4]

            # print(backendIO.toJSON(open_prompt, response_prompts))
            backendIO.send_question_to_frontend(open_prompt, response_prompts, time)

            response_id, response = backendIO.read_from_frontend(time, response_prompts)

            conversation.append((prompt_id, response_id))

            prompt_id = response.get_question_id()

        elif prompt_id in solution_prompts.keys():
            open_prompt = solution_prompts[prompt_id]

            # Truncate time down to the centisecond
            time = datetime.now().strftime("%Y%m%d%H%M%S%f")[0:-4]

            # print(backendIO.toJSON(open_prompt, response_prompts))
            backendIO.send_solution_to_frontend(open_prompt, info_listing_prompts, time)

            email_status, email_address = backendIO.read_from_frontend(time, response_prompts)

            rsolution = email_helper.solutionToRichSolution(open_prompt, info_listing_prompts)

            conversation.append((prompt_id, email_status))

            backendIO.store_conversation(conversation, time)

            conversation = []
            conversation.append(('Emotion', 'Null'))

            if email_status == 'emailTrue':
                email_helper.email_solutions(email_address, rsolution)

            prompt_id = '10'
        else:
            print('Bad prompt ID')

        # OLD CODE: CLI backend setup
        # response_id_list = open_prompt.get_response_ids()
        # print(open_prompt.get_text())
        # for response in response_id_list:
        #     if response in response_prompts.keys():
        #         print('{}: {}'.format(response_prompts[response].get_text(), response))
        # print('_____________________________')

        # selection = input('')
        # response_id = open_prompt.get_response_ids()[int(selection)]
        # response = response_prompts[response_id]
        # prompt_id = response.get_question_id()
        # print(prompt_id)
        # if prompt_id == '0':
        #     do_end = input('Enter anything to exit')
        #     if do_end != '':
        #         print('')
        #         break


if __name__ == "__main__":
    main()
