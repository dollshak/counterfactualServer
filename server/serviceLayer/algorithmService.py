from server.businessLayer.Algorithms.Algorithm import Algorithm
from server.businessLayer.AlgorithmsController import AlgorithmsController
from server.Tools.SystemConfig import SystemConfig


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
        return self.algorithms_controller.run_selected_algorithms(algorithms_names, arg_list, model, model_input)

    def remove_algorithm(self, name):
        raise Exception("Not implemented.")

    def get_algorithm_info(self, name):
        raise Exception("Not implemented.")

    def get_algorithm_code(self, name):
        raise Exception("Not implemented.")

    def get_all_algorithms(self):
        raise Exception("Not implemented.")

    def edit_algorithm(self, algorithm):
        raise Exception("Not implemented.")
