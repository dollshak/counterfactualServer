from server.businessLayer.Algorithms.Algorithm import Algorithm
from server.businessLayer.AlgorithmsController import AlgorithmsController
from server.Tools.SystemConfig import SystemConfig
from server.businessLayer.Inputs_Handlers.InputOutputController import InputOutputController
from server.businessLayer.Inputs_Handlers.PickleModel import PickleModel
from server.Tools.Logger import Logger

logger = Logger()


class AlgorithmService:
    def __init__(self, config):
        self.config = config
        self.algorithms_controller = AlgorithmsController(self.config)

    def add_new_algorithm(self, file_content, name: str, argument_lst: list[dict], description: str,
                          additional_info: str,
                          output_example: list[str], algo_type: list[str]):
        try:
            self.algorithms_controller.add_new_algorithm(file_content, name, argument_lst, description, additional_info,
                                                         output_example, algo_type)
            return "ok"
        except:
            logger.error(f'Adding a new algorithm has failed.')  # TODO fix the except and add the message to the log
            return "exception"

    def run_algorithms(self, algorithms_names, model_content, arg_list, model_input):
        feature_names, feature_values = InputOutputController().handle_input(model_input)
        model = PickleModel.from_pickle_content(model_content)
        ress = self.algorithms_controller.run_selected_algorithms(algorithms_names, arg_list, model,
                                                                  feature_values,
                                                                  feature_names)
        logger.debug("handling outputs")
        dict = InputOutputController().handle_output(feature_names, feature_values, ress, algorithms_names)
        return dict

    def remove_algorithm(self, name):
        self.algorithms_controller.remove_algorithm(name)

    def get_algorithm_info(self, name):
        return self.algorithms_controller.get_algorithm(name)

    def get_algorithm_code(self, name):
        raise Exception("Not implemented.")

    def get_all_algorithms(self):
        return self.algorithms_controller.get_all_algorithms()

    def edit_algorithm(self, file_content, file_name: str, arguments_list: list[dict], description: str,
                       additional_info: str,
                       output_example: list[str],
                       algo_type):
        try:
            self.algorithms_controller.edit_algorithm(file_content, file_name, arguments_list, description,
                                                      additional_info,
                                                      output_example,
                                                      algo_type)
            return "ok"
        except:
            logger.error(f'Editing an algorithm has failed.')  # TODO fix the except and add the message to the log
            return "exception"
