import os, sys


class question_prompt:
    def __init__(self, text, response_ids):
        self.text = text
        self.response_ids = response_ids
        for i in response_ids:
            if i == '' or i == '\r':
                self.response_ids.remove(i)

    def get_text(self):
        return self.text

    def get_response_ids(self):
        return self.response_ids


class response_prompt:
    def __init__(self, text, question_id):
        self.text = text
        self.question_id = question_id

    def get_text(self):
        return self.text

    def get_response_ids(self):
        return self.question_id


def get_path(relative_path, file_name=''):
    '''
    Generate a path to a file to open. Uses the location of data_extract.py (this script) as a reference.
    --------
    Inputs:
    relative_path - str:
        A relative path from the location of this script to the location of the target directory or file
    file_name - str:
        Optional: The name of the file to open.
        Not required if the file_name is added to 'relative_path'
        Useful for making neat, automated calls of get_path()
    --------
    Output: A path towards a target file
    '''
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path + file_name))
    return file_path


def load_spreadsheet(spreadsheet, prompt_type):
    '''
    prompt_type:
        Use "question" for question_prompt
        Use "response" for response_prompt
    '''
    # spreadsheet.open() or something
    file_path = get_path(spreadsheet)
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
                prompt_dict[prompt_id] = question_prompt(text, response_ids)
            if prompt_type == 'response':
                question_id = data[2]
                prompt_dict[prompt_id] = response_prompt(text, question_id)
        except Exception as e:
            print('Error in load_spreadsheet: {} --> {}'.format(split_spreadsheet[line], e))
    return prompt_dict


def get_response_texts(response_id_list, response_prompts_dict):
    response_texts = []
    for response_id in response_id_list:
        response_texts.append(response_prompts_dict[response_id].get_text())
    return response_texts

# Examples of valid commands:
# python3 backend.py
# python3 backend.py Test_Tree_Question_Prompts.csv Test_Tree_Response_Prompts.csv
def main():
    question_prompt_filename = 'Example_Decision_Tree_Question_Prompts.csv'
    response_prompt_filename = 'Example_Decision_Tree_Response_Prompts.csv'

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
        prompt_id = response.get_response_ids()
        print(prompt_id)


if __name__ == "__main__":
    main()
