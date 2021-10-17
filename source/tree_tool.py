from backend import load_spreadsheet


class tree_node:
    def __init__(self, id_val, node_type=None, prompts=None):
        self.id_val = id_val
        self.node_type = node_type
        self.children = {}
        self.prompts = prompts

    def get_prompts(self):
        return self.prompts

    def get_node_type(self):
        return self.node_type

    def add_child(self, child_id, child_prompt, child_type):
        try:
            if self.children[child_id + child_type] is not None:
                print('Duplicate key {}: not adding'.format(child_id + child_type))
                if child_type == '-Q':
                    print('WARNING: POSSIBLE CYCLE DETECTED')
                    print('key: {}\nprompt: {}\ntype: {}'.format(child_id, child_prompt, child_type))
                    # raise RecursionError('key: {}\nprompt: {}\ntype: {}'.format(child_id, child_prompt, child_type))
            else:
                self.children[child_id + child_type] = tree_node(child_id, child_type, child_prompt)
        except KeyError:
            self.children[child_id + child_type] = child_prompt

    def add_child_from_node(self, node, child_id, child_type):
        try:
            if self.children[child_id + child_type] is not None:
                print('Duplicate key {}: not adding'.format(child_id + child_type))
                if child_type == '-Q':
                    print('WARNING: POSSIBLE CYCLE DETECTED')
                    print('key: {}\ntype: {}'.format(child_id, child_type))
                    # raise RecursionError('key: {}\nprompt: {}\ntype: {}'.format(child_id, child_prompt, child_type))
            else:
                self.children[child_id + child_type] = node
        except KeyError:
            self.children[child_id + child_type] = node

    def get_children(self):
        return self.children

    # def create_children(self):
    #     for prompt in self.prompts:
    #         if self.node_type is 'question':
    #             self.children.append(tree_node(id_val=prompt, node_type='response', prompts=None))
    #     # def check_for_cycle(self):


def check_tree():
    '''
    This entire function may be unneccesary
    '''
    print("Checking Trees in Student_Sentiment_Sensor/data/")
    spreadsheet_questions = load_spreadsheet('../data/' + 'Test_Tree_Question_Prompts.csv', 'question')
    spreadsheet_responses = load_spreadsheet('../data/' + 'Test_Tree_Response_Prompts.csv', 'response')
    node_dict = {}

    for key in spreadsheet_questions.keys():
        responses_ids = spreadsheet_questions[key].get_response_ids()
        node_dict[key + '-Q'] = tree_node(key, node_type='-Q', prompts=responses_ids)

    for key in spreadsheet_responses.keys():
        question_id = spreadsheet_responses[key].get_question_id()
        node_dict[key + '-R'] = tree_node(id_val=key, node_type='-R', prompts=question_id)

        # for response_id in responses_ids:
        #     response_text = spreadsheet_responses[response_id].get_text()
        # node_dict[key].add_child(child_id=response_id, child_prompt=response_text, child_type='-R')
        # print(key, spreadsheet_questions[key].get_text(), node_dict[key].get_children())

    for key, value in node_dict.items():
        print(key, value.get_prompts())

    print('Finished creating trees in Student_Sentiment_Sensor/data/')


if __name__ == "__main__":
    check_tree()
