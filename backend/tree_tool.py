'''
Tree checking tool

CURRENTLY OBSOLETE (2021-26-11)
    - Does not check for "solution" or "info listing" prompts
        - Needs solution_prompt support
        - Needs info_listing_prompt support
    - Updating this is LOW PRIORITY and can likely be avoided for this capstone
'''


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
        '''
        Unusued Function
        '''
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

    def navigate_tree(self, node=self):
        current_node = self
        print(current_node.get_prompts)  # useless temp line
        if type(self.prompts) is list:
            for next_node in self.prompts:
                self.navigate_tree(next_node)
                print(next_node)
        elif type(self.prompts) is str:
            print(self.prompts)
            if self.prompts != '0':
                self.navigate_tree(self.prompts)

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
    question_tag = '-Q'
    response_tag = '-R'

    for key in spreadsheet_questions.keys():
        responses_ids = spreadsheet_questions[key].get_response_ids()
        node_dict[key + '-Q'] = tree_node(key, node_type=question_tag, prompts=responses_ids)

    for key in spreadsheet_responses.keys():
        question_id = spreadsheet_responses[key].get_question_id()
        node_dict[key + '-R'] = tree_node(id_val=key, node_type=response_tag, prompts=question_id)

    for key in node_dict.keys():
        prompts = node_dict[key].get_prompts()

        # Add responses (children) to questions (parent)
        if question_tag in key and type(prompts) is list:
            for response_id in node_dict[key].get_prompts():
                try:
                    node_dict[key].add_child_from_node(node=node_dict[response_id + response_tag],
                                                       child_id=response_id,
                                                       child_type=response_tag)
                except KeyError as e:
                    print('KeyError: {} was not generated/attached. Tree may have a hole.'.format(e))
        if response_tag in key:
            question_id = node_dict[key].get_prompts()
            if question_id != '0':
                try:
                    node_dict[key].add_child_from_node(node=node_dict[question_id + question_tag],
                                                       child_id=question_id,
                                                       child_type=question_tag)
                except KeyError as e:
                    print('KeyError: {} was not generated/attached. Tree may have a hole.'.format(e))

    node_dict['0' + question_tag].navigate_tree()
    # node_dict['1553-R'].navigate_tree()
    print('Finished creating trees in Student_Sentiment_Sensor/data/')


if __name__ == "__main__":
    check_tree()
