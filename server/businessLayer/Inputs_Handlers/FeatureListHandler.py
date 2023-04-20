from server.businessLayer.Inputs_Handlers.InputHandlerAbstract import InputHandlerAbstract


class FeatureListHandler(InputHandlerAbstract):

    def __init__(self):
        super().__init__("FeatureList")

    def prepare_input(self, model_input):
        raise Exception("Not implemented")

    def prepare_output(self):
        raise Exception("Not implemented")
