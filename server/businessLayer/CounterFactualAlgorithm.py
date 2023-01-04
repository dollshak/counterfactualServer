from server.businessLayer.Logger import Logger
from server.businessLayer.MlModel import MlModel
from server.businessLayer.ArgumentDescription import ArgumentDescription


class CounterFactualAlgorithm:
    def __init__(self, model: MlModel, name: str, argument_lst: list[ArgumentDescription], description: str,
                 additional_info: str, output_example: list[str]):
        self.model = model
        self.name = name
        self.argument_lst = argument_lst
        self.description = description
        self.additional_info = additional_info
        self.output_example = output_example

    def explain(self, model_input) -> list:
        raise Exception(f'counterfactual algorithm {self.name} does not override explain method')
