class question_prompt:
    def __init__(self, text, response_ids):
        self.text = text
        self.response_ids = list(filter(None, response_ids))

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
