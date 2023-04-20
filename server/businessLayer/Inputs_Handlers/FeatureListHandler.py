from server.businessLayer.Inputs_Handlers.InputHandlerAbstract import InputHandlerAbstract


class FeatureListHandler(InputHandlerAbstract):

    def __init__(self):
        super().__init__("FeatureList")

    def prepare_input(self, model_input):
        feature_names = list()
        feature_values = list()
        for name, value in model_input.items():
            feature_names.append(name)
            feature_values.append(value)
        return feature_names, feature_values
    def prepare_output(self):
        raise Exception("Not implemented")
