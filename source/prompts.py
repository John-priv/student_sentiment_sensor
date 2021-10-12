class question_prompt:
    def __init__(self, text, response_ids):
        self.text = text
        self.response_ids = response_ids
        for i in response_ids:
            if i == '' or i == '\r\n' or i is '\n' or i is None or '\n' in i:
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
