class Algorithm:
    def __init__(self, name, description, code, parameters, article_link, additional_fields):
        self.article_link = article_link
        self.parameters = parameters
        self.code = code
        self.description = description
        self.name = name
        self.additional_fields = additional_fields

        raise Exception("Not implemented")