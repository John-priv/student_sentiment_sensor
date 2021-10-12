from backend import load_spreadsheet


class tree_node:
    def __init__(self, id_val, parent=None, children=None):
        self.id_val = id_val
        self.parent = parent
        self.children = children

    # def check_for_cycle(self):


def check_tree():
    print("Checking Trees in Student_Sentiment_Sensor/data/")
    spreadsheet_questions = load_spreadsheet('../data/' + 'Test_Tree_Question_Prompts.csv', 'question')
    spreadsheet_responses = load_spreadsheet('../data/' + 'Test_Tree_Response_Prompts.csv', 'response')

    for key, value in spreadsheet_questions.items():
        print(key, value)


if __name__ == "__main__":
    check_tree()
