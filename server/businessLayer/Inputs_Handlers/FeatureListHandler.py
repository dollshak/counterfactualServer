import random

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

    # TODO remove algo_times default
    def prepare_output(self, feature_names, feature_values, cfs_results, algorithms_names, model_result, algo_times:dict,
                       error_messages={}):
        """
        example output
        {
            'input': {
                'name': 'ido',
                'age': 25,
                'height': 183,
                'living area': 'rural'
                'modelResult': 0.56
            },
            'output': {
                'algo1': {
                    "time" : 0.55,
                    "results" : [['ido', 27, 183, 'rural'], ['ido', 25, 189, 'rural']]
                    "errorMessage": ""
                    },
                'algo2': {
                    "time" : 0.20,
                    "results" : [['ido', 27, 183, 'rural'], ['ido', 25, 189, 'rural']]
                    "errorMessage": ""
                    },
                'failed_algo': {
                    "time" : 0.20,
                    "results" : []
                    "errorMessage": "error occurred for some reason"

                    },
            }
        }
        :param model_result:
        :param feature_names:
        :param feature_values:
        :param cfs_results:
        :param algorithms_names:
        :return:
        """
        output = {}
        for algo_name, res in zip(algorithms_names, cfs_results):
            output[algo_name] = {}
            output[algo_name]['results'] = res
            # TODO if condition
            if algo_name in algo_times.keys():
                output[algo_name]['time'] = algo_times[algo_name]
            else:
                output[algo_name]['time'] = -1
            # TODO if condition
            if algo_name in error_messages.keys():
                output[algo_name]['errorMessage'] = error_messages[algo_name]
            else:
                output[algo_name]['errorMessage'] = ""
        input = {'model_result':model_result}
        for name, val in zip(feature_names, feature_values):
            input[name] = val
        # TODO change hard coded here
        ################################################################################
        input['model_result'] = model_result
        ################################################################################
        ################################################################################
        dict = {'input': input, 'output': output}
        return dict
