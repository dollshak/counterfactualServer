class ArgumentDescriptionDto:
    def __init__(self, param_name: str, description: str, accepted_types: list[str],default_value):
        self.param_name = param_name
        self.description = description
        self.accepted_types = accepted_types
        self.default_value = default_value

    def serialize(self):
        return {
            'param_name': self.param_name,
            'description': self.description,
            'accepted_types': self.accepted_types,
            'default_value': self.default_value,
        }