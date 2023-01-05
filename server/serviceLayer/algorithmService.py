from server.businessLayer.Algorithm import Algorithm
from server.businessLayer.AlgorithmsController import AlgorithmsController
from server.businessLayer.SystemConfig import SystemConfig


class AlgorithmService:
    def __init__(self):
        self.algorithms_controller = AlgorithmsController(SystemConfig())

    def add_new_algorithm(self, filename, file, name, list=[]):
        try:
            algorithm = Algorithm(name, list,filename)
            self.algorithms_controller.add_new_algorithm(file,algorithm)
            return "ok"
        except :
            return "exception"


    def run_algorithms(self, algorithm_name, model, arg_list, model_input):
        return self.algorithms_controller.run_selected_algorithms(algorithm_name, model, arg_list, model_input)

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
