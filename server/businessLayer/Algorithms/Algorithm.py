from abc import abstractmethod
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription


class Algorithm:
    def __init__(self, cf_args: list, model):
        self.cf_args = cf_args
        self.model = model

    @abstractmethod
    def explain(self, model_input):
        pass
