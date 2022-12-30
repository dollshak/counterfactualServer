from abc import abstractmethod

from server.businessLayer.MlModel import MlModel
from server.businessLayer.argumentDescription import argumentDescription


class Algorithm:
    def __init__(self, name, file, args_desc: list[argumentDescription], model: MlModel):
        self.model = model
        self.file = file
        self.args_desc = args_desc
        self.name = name

    @abstractmethod
    def explain(self, model_input):
        pass
