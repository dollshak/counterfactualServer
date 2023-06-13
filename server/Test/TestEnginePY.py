import unittest
from server.Test.additionals.Model_For_test import ModelForTest
from server.Test.additionals.TestConfig import TestConfig
from server.Test.additionals.TestUtils import TestUtils
from server.Tools.FailedCFException import FailedCFException
from server.Tools.ModelException import ModelException
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.Engine.EnginePY import EnginePY
from server.businessLayer.FileManager import FileManager


class TestEnginePY(unittest.TestCase):
    def test_valid_inputs(self):
        reg_model = self.model_class.get_regression_model()
        engine = EnginePY(reg_model, "DiCE_for_test.py", self.cf_args, TestConfig(),TestUtils.get_model_feature_names())
        algo_time_limit = self.cf_args["time_limit"]
        res = engine.run_algorithm(self.x_test, algo_time_limit=algo_time_limit)
        self.assertTrue(len(res) > 0 and len(res[0]) > 0)

    # def test_invalid_model(self):
    #  TODO implement test here!

    #     reg_model = {}
    #     engine = EnginePY(reg_model, "DiCE_for_test.py", self.cf_args, TestConfig())
    #     try:
    #         res = engine.run_algorithm(self.x_test)
    #         assert False
    #     except ModelException as e:
    #         # TODO instead of assert true, assert equals e (exception message) with
    #         #  the relevant message (need to write it)
    #         assert True
    #     except:
    #         assert False

    def test_unexisting_cf(self):
        reg_model = self.model_class.get_regression_model()
        invalid_args = self.cf_args.copy()
        del invalid_args['features']
        invalid_CF_name = "DiCE_for_test_invalid.py"
        try:
            engine = EnginePY(reg_model, invalid_CF_name, invalid_args, TestConfig(),list(self.cf_args["features"]))
            assert False
        except FailedCFException as e:
            self.assertEqual(f'There is no CF algorithm named:{invalid_CF_name}', e.message)
            assert True
        except:
            assert False

    def test_missing_cf_argument(self):
        reg_model = self.model_class.get_regression_model()
        invalid_args = self.cf_args.copy()
        del invalid_args['features']
        try:
            engine = EnginePY(reg_model, "DiCE_for_test.py", invalid_args, TestConfig(),list(self.cf_args["features"]))
            res = engine.run_algorithm(self.x_test, algo_time_limit=5)
            assert False
        except FailedCFException as e:
            self.assertEqual( f'not enough arguments given for {self.algo_name}', e.message)
        except:
            assert False

    def test_argument_name_changed(self):
        reg_model = self.model_class.get_regression_model()
        invalid_args = self.cf_args.copy()
        invalid_args['features_2'] = invalid_args['features']
        del invalid_args['features']
        try:
            engine = EnginePY(reg_model, "DiCE_for_test.py", invalid_args, TestConfig(),list(self.cf_args["features"]))
            res = engine.run_algorithm(self.x_test, algo_time_limit=5)
            assert False
        except FailedCFException as e:
            self.assertEqual(f'features is missing for {self.algo_name}', e.message)
            assert True
        except:
            assert False

    def test_additional_argument(self):
        reg_model = self.model_class.get_regression_model()
        invalid_args = self.cf_args.copy()
        invalid_args['f'] = 3
        try:
            engine = EnginePY(reg_model, "DiCE_for_test.py", invalid_args, TestConfig(),list(self.cf_args["features"]))
            assert False
        except FailedCFException as e:
            self.assertEqual(f'too many arguments given for {self.algo_name}', e.message)
        except:
            assert False

    def setUp(self) -> None:
        self.cf_args = {"features": {}}
        self.x_test = self.model_class.x_val_clf[0]

        self.cf_args['features'] = {
            'income': [2500, 40000],
            'outcome': [2500, 20000],
            'total': [10000, 200000],
            'loan': [25000, 1000000]
        }
        self.cf_args['outcome_name'] = 'label'
        self.cf_args['total_CFs'] = 4
        self.cf_args['desired_class'] = 2
        self.cf_args['desired_range'] = [0.8, 1.0]
        self.cf_args['is_classifier'] = False
        self.cf_args["time_limit"] = 5

    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:

        cls.model_class = ModelForTest()
        cls.algo_name = TestUtils.get_dice_algo_name()

        file_manager = FileManager(TestConfig())
        cf_description = TestUtils.get_dice_cf_description()
        file_manager.remove_algorithm(cls.algo_name)
        if not file_manager.is_algo_exist_in_db(cls.algo_name):
            file_manager.add_algorithm(TestUtils.get_dice_content(), cf_description)

    @classmethod
    def tearDownClass(cls) -> None:
        file_manager = FileManager(TestConfig())
        file_manager.clear_db()
        if file_manager.is_algo_exist_in_db("DiCE_for_test"):
            file_manager.remove_algorithm("DiCE_for_test")
