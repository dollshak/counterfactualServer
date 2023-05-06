class ArgumentDescription:
    def __init__(self, param_name: str, description: str, accepted_types: list[type]):
        self.param_name = param_name
        self.description = description
        self.accepted_types = accepted_types
