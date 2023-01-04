from abc import abstractmethod

from server.businessLayer.MlModel import MlModel
from server.businessLayer.ArgumentDescription import ArgumentDescription


class Algorithm:
    def __init__(self, name,  args_desc: list[ArgumentDescription], model: MlModel):
        self.model = model
        self.args_desc = args_desc
        self.name = name

    @abstractmethod
    def explain(self, model_input):
        pass
