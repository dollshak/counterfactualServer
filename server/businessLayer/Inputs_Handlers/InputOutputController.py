from server.businessLayer.Inputs_Handlers.FeatureListHandler import FeatureListHandler
from server.Tools.Logger import Logger

logger = Logger()


class InputOutputController:

    def __init__(self):
        pass

    def handle_input(self, model_input, input_type="FeatureList"):
        handler = self._get_handler(input_type)
        if not isinstance(model_input, dict):
            raise TypeError("Input for the model has to be in the shape of a dictionary")
        logger.debug("Starting to handle input before running algorithms.")
        return handler.prepare_input(model_input)

    def handle_output(self, feature_names, feature_values, cfs_results, algorithms_names, input_type="FeatureList"):
        handler = self._get_handler(input_type)
        logger.debug("Starting to handle output before displaying results to the user.")
        return handler.prepare_output(feature_names, feature_values, cfs_results, algorithms_names)

    def _get_handler(self, input_type):
        handler = None
        if FeatureListHandler().canHandle(input_type):
            handler = FeatureListHandler()

        if handler is None:
            raise Exception('invalid input_type')
        return handler
