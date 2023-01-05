from abc import abstractmethod

from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription


class Algorithm:
    def __init__(self,  cf_args:list, ):
        self.args_desc = args_desc
        self.name = name
        self.filename = filename

    @abstractmethod
    def explain(self, model_input):
        pass
