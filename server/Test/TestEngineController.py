import unittest
import random
import os

from server.Test.additionals.Model_For_test import ModelForTest
from server.Test.additionals.TestConfig import TestConfig
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.Engine.EngineController import EngineController
from server.businessLayer.FileManager import FileManager


class TestEngineController(unittest.TestCase):
    def test_time_pass_out(self):
        # TODO implement here when time is implemented
        assert False

    def test_run_one_cf(self):
        if not self.file_manager.is_algo_exist_in_db(self.algo_name):
            self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)

        inputs = {self.algo_name: self.cf_input}
        result = self.controller.run_algorithms([self.algo_name], self.model, self.x_test, inputs)
        self.assertGreater(len(result[0]), 0)

    def test_run_multiple_cf(self):
        if not self.file_manager.is_algo_exist_in_db(self.algo_name):
            self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        if not self.file_manager.is_algo_exist_in_db(self.algo_name_2):
            self.file_manager.add_algorithm(self.test_cf_content, self.cf_description_2)

        inputs = {self.algo_name: self.cf_input,
                  self.algo_name_2: self.cf_input}
        result = self.controller.run_algorithms([self.algo_name, self.algo_name_2], self.model, self.x_test, inputs)
        self.assertGreater(len(result[0]), 0)
        self.assertGreater(len(result[1]), 0)

    def test_run_invalid_cf(self):
        if not self.file_manager.is_algo_exist_in_db(self.algo_name):
            self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        invalid_cf_inputs = self.cf_input.copy()
        del invalid_cf_inputs['features']
        invalid_inputs = {self.algo_name: invalid_cf_inputs}
        result = self.controller.run_algorithms([self.algo_name], self.model, self.x_test, invalid_inputs)
        self.assertTrue(isinstance(result, list))
        self.assertTrue(isinstance(result[0], list))
        self.assertTrue((len(result[0]) == 0))

    def test_run_invalid_cf_of_many(self):
        if not self.file_manager.is_algo_exist_in_db(self.algo_name):
            self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        if not self.file_manager.is_algo_exist_in_db(self.algo_name_2):
            self.file_manager.add_algorithm(self.test_cf_content, self.cf_description_2)
        invalid_cf_inputs = self.cf_input.copy()
        del invalid_cf_inputs['features']
        inputs = {self.algo_name: invalid_cf_inputs,
                          self.algo_name_2: self.cf_input}
        result = self.controller.run_algorithms([self.algo_name, self.algo_name_2], self.model, self.x_test, inputs)
        self.assertTrue(isinstance(result, list))
        self.assertTrue(isinstance(result[0], list))
        self.assertTrue((len(result[0]) == 0))
        self.assertTrue((len(result[1]) > 0))

    def setUp(self) -> None:
        rand_num = random.randint(1, 10000)
        file_name = 'DiCE_for_test'
        self.algo_name = file_name + '_' + str(rand_num)

        rand_num = random.randint(1, 10000)
        self.algo_name_2 = file_name + '_' + str(rand_num)
        with open('additionals/' + file_name + '.py', 'r') as file:
            self.test_cf_content = file.read()
        agd = [ArgumentDescription("age", "years old", ["str"])]
        desc = "tell you what your age is"
        self.desc = desc
        addI = "additional"
        self.addI = addI
        res_example = ["25"]
        self.res_example = res_example
        self.agd = agd
        self.file_manager = FileManager(TestConfig())
        cf_description = CounterFactualAlgorithmDescription(self.algo_name, agd, desc, addI, res_example,
                                                            "regressor")
        cf_description_2 = CounterFactualAlgorithmDescription(self.algo_name_2, agd, desc, addI, res_example,
                                                              "regressor")
        self.cf_description = cf_description
        self.cf_description_2 = cf_description_2
        self.controller = EngineController()

    def tearDown(self) -> None:
        self.file_manager.remove_algorithm(self.algo_name)
        self.file_manager.remove_algorithm(self.algo_name_2)

    @classmethod
    def setUpClass(cls) -> None:
        cls.model_class = ModelForTest()
        cls.model = cls.model_class.get_regression_model()
        cls.x_test = cls.model_class.x_val_clf[0]

        cls.cf_input = {
            "features":
                {
                    "income": [2500, 40000],
                    "outcome": [2500, 20000],
                    "total": [10000, 200000],
                    "loan": [25000, 1000000]
                },
            "outcome_name": "label",
            "total_CFs": 4,
            "desired_class": 2,
            "desired_range": [0.8, 1.0],
            "is_classifier": False
        }
