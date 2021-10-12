from backend import load_spreadsheet


class tree_node:
    def __init__(self, id_val, node_type=None, prompts=None):
        self.id_val = id_val
        self.node_type = node_type
        self.children = None
        self.prompts = prompts

    def get_prompts(self):
        return self.prompts

    def get_node_type(self):
        return self.node_type

    def add_child(self, child_id, child_type, child_prompts):
        print('temp')

    # def create_children(self):
    #     for prompt in self.prompts:
    #         if self.node_type is 'question':
    #             self.children.append(tree_node(id_val=prompt, node_type='response', prompts=None))
    #     # def check_for_cycle(self):


def check_tree():
    print("Checking Trees in Student_Sentiment_Sensor/data/")
    spreadsheet_questions = load_spreadsheet('../data/' + 'Test_Tree_Question_Prompts.csv', 'question')
    spreadsheet_responses = load_spreadsheet('../data/' + 'Test_Tree_Response_Prompts.csv', 'response')

    for key, value in spreadsheet_questions.items():
        print(key, value)


if __name__ == "__main__":
    check_tree()
