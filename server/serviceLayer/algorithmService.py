from server.businessLayer.Algorithms.Algorithm import Algorithm
from server.businessLayer.AlgorithmsController import AlgorithmsController
from server.Tools.SystemConfig import SystemConfig
from server.businessLayer.Inputs_Handlers.InputOutputController import InputOutputController


class AlgorithmService:
    def __init__(self):
        self.algorithms_controller = AlgorithmsController()

    def add_new_algorithm(self, file_content, name: str, argument_lst: list[dict], description: str,
                          additional_info: str,
                          output_example: list[str]):
        try:
            self.algorithms_controller.add_new_algorithm(file_content, name, argument_lst, description, additional_info,
                                                         output_example)
            return "ok"
        except:
            return "exception"

    def run_algorithms(self, algorithms_names, model, arg_list, model_input):
        feature_names, feature_values = InputOutputController().handle_input(model_input)
        ress = self.algorithms_controller.run_selected_algorithms(algorithms_names, arg_list, model, feature_values, feature_names)
        dict = InputOutputController.handle_output(feature_names,feature_values,ress,algorithms_names)
        return dict

    def remove_algorithm(self, name):
        raise Exception("Not implemented.")

    def get_algorithm_info(self, name):
        return self.algorithms_controller.get_algorithm(name)

    def get_algorithm_code(self, name):
        raise Exception("Not implemented.")

    def get_all_algorithms(self):
        return self.algorithms_controller.get_all_algorithms()

    def edit_algorithm(self, algorithm):
        raise Exception("Not implemented.")
