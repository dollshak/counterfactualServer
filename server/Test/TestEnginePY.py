import unittest

from server.Test.additionals.DiCE_for_test import DiCE_for_test
from server.Test.additionals.Model_For_test import ModelForTest


class TestEnginePY(unittest.TestCase):
    def test_valid_inputs(self):
        x_test = self.model_class.x_val_clf[0]
        reg_model = self.model_class.get_regression_model()
        dice = DiCE_for_test()
        dice.explain()
        # TODO need to implement here
        assert False

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
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.model_class = ModelForTest()
