from server.businessLayer.Inputs_Handlers.FeatureListHandler import FeatureListHandler


class InputOutputController:

    def __init__(self):
        pass

    def handle_input(self, model_input, input_type="FeatureList"):
        handler = self._get_handler(input_type)

        return handler.prepare_input(model_input)

    def handle_output(self, feature_names, feature_values, cfs_results, algorithms_names, input_type):
        handler = self._get_handler(input_type)
        return handler.prepare_output(feature_names, feature_values, cfs_results,algorithms_names)

    def _get_handler(self, input_type):
        handler = None
        if FeatureListHandler().canHandle(input_type):
            handler = FeatureListHandler()

        if handler is None:
            raise Exception('invalid input_type')
        return handler
