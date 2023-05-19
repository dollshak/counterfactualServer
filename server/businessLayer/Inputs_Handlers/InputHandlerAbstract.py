class InputHandlerAbstract:

    def __init__(self, input_type):
        self.input_type = input_type

    def prepare_input(self, model_input):
        """
        :param model_input: {'income' :3000, 'outcomes' [100,4000,300]}
        :returns tuple(feature_names, list(feature_values)) -> (['income', 'outcome'], [3000,[100,4000,300]])
        """
        pass

    def prepare_output(self, feature_names, feature_values, cfs_results, algorithms_names,model_result,algo_times,error_messages):
        pass

    def canHandle(self, input_type):
        return self.input_type == input_type
