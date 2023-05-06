class ArgumentDescriptionDto:
    def __init__(self, param_name: str, description: str, accepted_types: list[type]):
        self.param_name = param_name
        self.description = description
        self.accepted_types = accepted_types

    def serialize(self):
        return {
            'param_name': self.param_name,
            'description': self.description,
            'accepted_types': self.accepted_types,
        }