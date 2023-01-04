class ArgumentDescriptionDto:
    def __init__(self, name: str, description: str, accepted_types: list[type]):
        self.name = name
        self.description = description
        self.accepted_types = accepted_types

