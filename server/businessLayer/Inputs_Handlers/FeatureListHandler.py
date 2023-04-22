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

    def prepare_output(self, feature_names, feature_values, cfs_results, algorithms_names):
        output = {}
        for algo_name, res in zip(algorithms_names, cfs_results):
            output[algo_name] = res
        input = {}
        for name, val in zip(feature_names, feature_values):
            input[name] = val
        dict = {'input': input, 'output': output}
        return dict
