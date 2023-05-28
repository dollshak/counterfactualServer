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
        feature_names = model_input['names']
        feature_values = model_input['values']
        if len(feature_names) != len(feature_values):
            raise ValueError(f'Feature names has the length of {len(feature_names)} but feature vales has the length of'
                             f'{len(feature_values)}.They need to have equal length.')
        return feature_names, feature_values

    def prepare_output(self, feature_names:list, feature_values:list, cfs_results, algorithms_names, model_result,
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
        input = {}
        feature_names.append("modelResult")
        feature_values.append(model_result[0])
        input["values"] = feature_values
        input["names"] = feature_names
        dict = {'input': input, 'output': output}
        return dict
