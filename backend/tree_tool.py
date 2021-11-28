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
            # if self.children[child_id + child_type] is not None:
            if self.children[child_id] is not None:
                print('Duplicate key {}: not adding'.format(child_id + child_type))
                if child_type == '-Q':
                    print('WARNING: POSSIBLE CYCLE DETECTED')
                    print('key: {}\nprompt: {}\ntype: {}'.format(child_id, child_prompt, child_type))
                    # raise RecursionError('key: {}\nprompt: {}\ntype: {}'.format(child_id, child_prompt, child_type))
            else:
                # self.children[child_id + child_type] = tree_node(child_id, child_type, child_prompt)
                self.children[child_id] = tree_node(child_id, child_type, child_prompt)
        except KeyError:
            # self.children[child_id + child_type] = child_prompt
            self.children[child_id] = child_prompt

    def add_child_from_node(self, node, child_id, child_type):
        try:
            # if self.children[child_id + child_type] is not None:
            if self.children[child_id] is not None:
                # print('Duplicate key {}: not adding'.format(child_id + child_type))
                print('Duplicate key {}: not adding'.format(child_id))
                if child_type == '-Q':
                    print('WARNING: POSSIBLE CYCLE DETECTED')
                    # print('key: {}\ntype: {}'.format(child_id, child_type))
                    print('key: {}\ntype: {}'.format(child_id, child_type))
                    # raise RecursionError('key: {}\nprompt: {}\ntype: {}'.format(child_id, child_prompt, child_type))
            else:
                # self.children[child_id + child_type] = node
                self.children[child_id] = node
        except KeyError:
            # self.children[child_id + child_type] = node
            self.children[child_id] = node

    def get_children(self):
        return self.children

    def navigate_tree(self, node=None, visited_nodes=[], node_dict={}):
        current_node = self
        visited_nodes.append(self.id_val)
        print(current_node.get_prompts())  # useless temp line
        if type(self.prompts) is list:
            for next_node in self.prompts:
                print(next_node)
                if next_node not in visited_nodes:
                    self.navigate_tree(node=node_dict[next_node], visited_nodes=visited_nodes, node_dict=node_dict)
                print(next_node)
        elif type(self.prompts) is str:
            print(self.prompts)
            if self.prompts != '10':
                if self.prompts not in visited_nodes:
                    self.navigate_tree(node=node_dict[self.prompts], visited_nodes=visited_nodes, node_dict=node_dict)
                else:
                    print(visited_nodes)

    # def create_children(self):
    #     for prompt in self.prompts:
    #         if self.node_type is 'question':
    #             self.children.append(tree_node(id_val=prompt, node_type='response', prompts=None))
    #     # def check_for_cycle(self):

    def generate_tree(self, node_dict):
        print('foo')


def check_tree():
    '''
    This entire function may be unneccesary
    '''
    print("Checking Trees in Student_Sentiment_Sensor/data/")
    # spreadsheet_questions = load_spreadsheet('../data/' + 'Test_Tree_Question_Prompts.csv', 'question')
    # spreadsheet_responses = load_spreadsheet('../data/' + 'Test_Tree_Response_Prompts.csv', 'response')

    starting_id = '10'

    question_prompt_filename = 'decision_tree/question_prompts.csv'
    response_prompt_filename = 'decision_tree/response_prompts.csv'
    solution_prompt_filename = 'decision_tree/solution_prompts.csv'
    info_listing_prompt_filename = 'decision_tree/info_listing_prompts.csv'

    question_prompts = load_spreadsheet('../data/' + question_prompt_filename, 'question')  # dict
    response_prompts = load_spreadsheet('../data/' + response_prompt_filename, 'response')  # dict
    solution_prompts = load_spreadsheet('../data/' + solution_prompt_filename, 'solution')
    info_listing_prompts = load_spreadsheet('../data/' + info_listing_prompt_filename, 'info_listing')

    node_dict = {}
    question_tag = '-Q'
    response_tag = '-R'
    solution_tag = '-S'
    info_list_tag = '-I'

    for key in question_prompts.keys():
        responses_ids = question_prompts[key].get_response_ids()
        # node_dict[key + '-Q'] = tree_node(key, node_type=question_tag, prompts=responses_ids)
        node_dict[key] = tree_node(key, node_type=question_tag, prompts=responses_ids)

    for key in response_prompts.keys():
        question_id = response_prompts[key].get_question_id()
        # node_dict[key + '-R'] = tree_node(id_val=key, node_type=response_tag, prompts=question_id)
        node_dict[key] = tree_node(id_val=key, node_type=response_tag, prompts=question_id)

    for key in solution_prompts.keys():
        info_listing_id = solution_prompts[key].get_info_listing_ids()
        node_dict[key] = tree_node(id_val=key, node_type=solution_tag, prompts=info_listing_id)

    for key in info_listing_prompts.keys():
        node_dict[key] = tree_node(id_val=key, node_type=info_list_tag, prompts=starting_id)

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
            if question_id != starting_id:
                try:
                    node_dict[key].add_child_from_node(node=node_dict[question_id + question_tag],
                                                       child_id=question_id,
                                                       child_type=question_tag)
                except KeyError as e:
                    print('KeyError: {} was not generated/attached. Tree may have a hole.'.format(e))

    # node_dict['10' + question_tag].navigate_tree(node=None, visited_nodes=[], node_dict=node_dict)
    node_dict['10'].navigate_tree(node=None, visited_nodes=[], node_dict=node_dict)
    # node_dict['1553-R'].navigate_tree()
    print('Finished creating trees in Student_Sentiment_Sensor/data/')


if __name__ == "__main__":
    check_tree()
