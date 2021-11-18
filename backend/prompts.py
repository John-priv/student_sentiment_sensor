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

    def get_question_id(self):
        return self.question_id


class solutions_prompt:
    def __init__(self, text, info_listing_ids):
        self.text = text
        self.info_listing_ids = list(filter(None, info_listing_ids))

    def get_text(self):
        return self.text

    def get_info_listing_ids(self):
        return self.info_listing_ids


class info_listing_prompt:
    def __init__(self, text, info_link):
        self.text = text
        self.info_link = info_link

    def get_text(self):
        return self.text

    def get_info_link(self):
        return self.info_link
