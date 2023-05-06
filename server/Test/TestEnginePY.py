import unittest

from server.Test.additionals.DiCE_for_test import DiCE_for_test
from server.Test.additionals.Model_For_test import ModelForTest
from server.businessLayer.Engine.EnginePY import EnginePY


class TestEnginePY(unittest.TestCase):
    def test_valid_inputs(self):
        reg_model = self.model_class.get_regression_model()
        engine = EnginePY(reg_model, "DiCE.py", self.cf_args)
        res = engine.run_algorithm(self.x_test)
        self.assertTrue(len(res) > 0 and len(res[0]) > 0)

    def test_invalid_model(self):
        # TODO need to implement here
        assert False

    def test_unexisting_cf(self):
        # TODO need to implement here
        assert False

    def test_invalid_cf_inputs(self):
        # TODO need to implement here
        assert False

    def test_invalid_model_inputs(self):
        # TODO need to implement here
        assert False

    def test_incompatible_model_to_cf(self):
        # TODO need to implement here
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