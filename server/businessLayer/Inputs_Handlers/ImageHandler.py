from server.businessLayer.Inputs_Handlers.InputHandlerAbstract import InputHandlerAbstract


class imageHandler(InputHandlerAbstract):
    def __init__(self):
        super().__init__("image")

    def prepare_input(self, model_input):
        super().prepare_input(model_input)

    def prepare_output(self):
        super().prepare_output()

    def canHandle(self, input_type):
        return super().canHandle(input_type)