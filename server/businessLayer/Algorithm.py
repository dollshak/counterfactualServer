from abc import abstractmethod

from server.businessLayer.ArgumentDescription import ArgumentDescription


class Algorithm:
    def __init__(self, name, args_desc: list[ArgumentDescription], filename: str):
        self.args_desc = args_desc
        self.name = name
        self.filename = filename

    @abstractmethod
    def explain(self, model_input):
        pass
