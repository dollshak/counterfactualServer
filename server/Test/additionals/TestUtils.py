from server.Test.additionals.TestConfig import TestConfig
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.FileManager import FileManager


class TestUtils:
    @staticmethod
    def get_dice_cf_description():
        algo_name = TestUtils.get_dice_algo_name()
        agd = [ArgumentDescription("features", "model data features", ["dict"]),
               ArgumentDescription("outcome_name", "target label name", ["str"]),
               ArgumentDescription("total_CFs", "number of result looking for", ["float"]),
               ArgumentDescription("desired_range", "accuracy required", ["list"]),
               ArgumentDescription("is_classifier", "one must tell whether is classifier or not", ["boolean"]),
               ArgumentDescription("desired_class", "class to change to", ["str"])]
        desc = "from library"
        addI = "No"
        res_example = ["1.2"]
        cf_description = CounterFactualAlgorithmDescription(algo_name, agd, desc, addI, res_example,
                                                            "regressor")
        return cf_description

    @staticmethod
    def get_dice_algo_name():
        return "DiCE_for_test"

    @staticmethod
    def get_dice_content():
        with open('additionals/' + TestUtils.get_dice_algo_name() + '.py', 'r') as file:
            test_cf_content = file.read()
            return test_cf_content

    @staticmethod
    def get_dice_arg_list():
        return [
            {"param_name": "features", "description": "features", "accepted_types": ["list"]},
            {"param_name": "outcome_name", "description": "target name", "accepted_types": ["string"]},
            {"param_name": "total_CFs", "description": "number of results", "accepted_types": ["float"]},
            {"param_name": "desired_class", "description": "class to find", "accepted_types": ["float"]},
            {"param_name": "desired_range", "description": "range of accuracy", "accepted_types": ["list"]},
            {"param_name": "is_classifier", "description": "kind of model", "accepted_types": ["boolean"]}
        ]

    @staticmethod
    def get_model_feature_names():
        return ["income" , "outcome", "total","loan"]

    @staticmethod
    def get_one_cf_input():
        return {}
