import random

from server.businessLayer.Inputs_Handlers.InputHandlerAbstract import InputHandlerAbstract


class FeatureListHandler(InputHandlerAbstract):

    def __init__(self):
        super().__init__("FeatureList")

    def prepare_input(self, model_input):
        """
        {
             values: [9562, 5060, 81991, 374286],
             names: ["income", "outcome", "total", "loan"]
            }
        :param model_input:
        :return:
        """
        # TODO raz need to create an exception if names and values aren't same size
        feature_names = model_input['names']
        feature_values = model_input['values']
        return feature_names, feature_values

    def prepare_output(self, feature_names, feature_values, cfs_results, algorithms_names, model_result,
                       algo_times: dict,
                       error_messages={}):
        """
        example output
        {
            'result_input': {
                values: [1,2,3,4,0.56]
                 names: ["param1", "param2", "param3", "param4", "modelResult"]
            },
            'output': {
                'algo1': {
                    "time" : 0.55,
                    "results" : [['ido', 27, 183, 'rural', 0,45], ['ido', 25, 189, 'rural', 0.80]]
                    "errorMessage": ""
                    },
                'algo2': {
                    "time" : 0.20,
                    "results" : [['ido', 27, 183, 'rural',0.9], ['ido', 25, 189, 'rural', 0.9]]
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
            if algo_name in algo_times.keys():
                output[algo_name]['time'] = algo_times[algo_name]
            else:
                output[algo_name]['time'] = -1
            if algo_name in error_messages.keys():
                output[algo_name]['errorMessage'] = error_messages[algo_name]
            else:
                output[algo_name]['errorMessage'] = ""
        #  TODO raz model result should be part of result_input.values
        #  TODO raz "modelResult" (the name) should be part of result_input.names
        input = {'model_result': model_result}
        for name, val in zip(feature_names, feature_values):
            input[name] = val
        input['model_result'] = model_result
        dict = {'input': input, 'output': output}
        return dict
