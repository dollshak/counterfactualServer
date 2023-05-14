import unittest
from server.Test.additionals.Model_For_test import ModelForTest
from server.Test.additionals.TestConfig import TestConfig
from server.Tools.FailedCFException import FailedCFException
from server.Tools.ModelException import ModelException
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.Engine.EnginePY import EnginePY
from server.businessLayer.FileManager import FileManager


class TestEnginePY(unittest.TestCase):
    def test_valid_inputs(self):
        reg_model = self.model_class.get_regression_model()
        engine = EnginePY(reg_model, "DiCE_for_test.py", self.cf_args, TestConfig())
        res = engine.run_algorithm(self.x_test)
        self.assertTrue(len(res) > 0 and len(res[0]) > 0)

    def test_invalid_model(self):
        reg_model = {}
        engine = EnginePY(reg_model, "DiCE_for_test.py", self.cf_args, TestConfig())
        try:
            res = engine.run_algorithm(self.x_test)
            assert False
        except ModelException as e:
            # TODO instead of assert true, assert equals e (exception message) with
            #  the relevant message (need to write it)
            assert True
        except:
            assert False

    def test_unexisting_cf(self):
        reg_model = self.model_class.get_regression_model()
        invalid_args = self.cf_args.copy()
        del invalid_args['features']
        engine = EnginePY(reg_model, "DiCE_for_test_invalid.py", invalid_args, TestConfig())
        try:
            res = engine.run_algorithm(self.x_test)
            assert False
        except FailedCFException as e:
            # TODO instead of assert true, assert equals e (exception message) with
            #  the relevant message (need to write it)
            #  error should be raised from EnginePy on validate
            assert True
        except:
            assert False

    def test_missing_cf_argument(self):
        reg_model = self.model_class.get_regression_model()
        invalid_args = self.cf_args.copy()
        del invalid_args['features']
        engine = EnginePY(reg_model, "DiCE_for_test.py", invalid_args, TestConfig())
        try:
            res = engine.run_algorithm(self.x_test)
            assert False
        except FailedCFException as e:
            self.assertEqual(e, f'not enough arguments given for DiCE_for_test')
        except:
            assert False

    def test_argument_name_changed(self):
        reg_model = self.model_class.get_regression_model()
        invalid_args = self.cf_args.copy()
        invalid_args['features_2'] = invalid_args['features']
        del invalid_args['features']
        engine = EnginePY(reg_model, "DiCE_for_test.py", invalid_args, TestConfig())
        try:
            res = engine.run_algorithm(self.x_test)
            assert False
        except FailedCFException as e:
            # TODO instead of assert true, assert equals e (exception message) with
            #  the relevant message (need to write it) - this one should be like missing argument
            assert True
        except:
            assert False

    def test_additional_argument(self):
        reg_model = self.model_class.get_regression_model()
        invalid_args = self.cf_args.copy()
        invalid_args['f'] = 3
        engine = EnginePY(reg_model, "DiCE_for_test.py", invalid_args, TestConfig())
        try:
            res = engine.run_algorithm(self.x_test)
            assert False
        except FailedCFException as e:
            # TODO instead of assert true, assert equals e (exception message) with
            #  the relevant message (need to write it)
            assert True
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

    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.model_class = ModelForTest()
        cls.algo_name = "DiCE_for_test"
        file_manager = FileManager(TestConfig())

        with open('additionals/' + cls.algo_name + '.py', 'r') as file:
            test_cf_content = file.read()
        # TODO need to fix arguments here to be like in setup
        agd = [ArgumentDescription("age", "years old", ["str"])]
        desc = "tell you what your age is"
        addI = "additional"
        res_example = ["25"]
        file_manager = FileManager(TestConfig())
        cf_description = CounterFactualAlgorithmDescription(cls.algo_name, agd, desc, addI, res_example,
                                                            "regressor")
        if not file_manager.is_algo_exist_in_db(cls.algo_name):
            file_manager.add_algorithm(test_cf_content, cf_description)

    @classmethod
    def tearDownClass(cls) -> None:
        file_manager = FileManager(TestConfig())
        if file_manager.is_algo_exist_in_db("DiCE_for_test"):
            file_manager.remove_algorithm("DiCE_for_test")
