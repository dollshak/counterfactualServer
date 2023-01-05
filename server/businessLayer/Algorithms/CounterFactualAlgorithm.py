from server.businessLayer.ML_Models.MlModel import MlModel
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription


class CounterFactualAlgorithm:
    def __init__(self,  name: str, argument_lst: list[ArgumentDescription], description: str,
                 additional_info: str, output_example: list[str]):
        self.name = name
        self.argument_lst = argument_lst
        self.description = description
        self.additional_info = additional_info
        self.output_example = output_example

    def explain(self, model_input) -> list:
        raise Exception(f'counterfactual algorithm {self.name} does not override explain method')
