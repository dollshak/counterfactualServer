import unittest
import random

from pandocfilters import Math

from server.Test.additionals.TestConfig import TestConfig
from server.Test.additionals.TestUtils import TestUtils
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.AlgorithmsController import AlgorithmsController
from server.businessLayer.Engine.EnginePY import EnginePY
from server.businessLayer.FileManager import FileManager


class TestAlgorithmController(unittest.TestCase):

    def test_restore_algorithm(self):
        # this test that algorithm is imported when calling get all algorithms

        # setting start position -> algo in db but not in system
        self.cf_description.name = self.algo_name
        if not self.file_manager.is_algo_exist_in_db(self.algo_name):
            self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        # remove from system
        self.file_manager.remove_algo_system(self.algo_name)
        if self.file_manager.is_algo_exist_in_system(self.algo_name):
            assert False

        # test body
        algos = self.controller.get_all_algorithms()
        algo_exist = False
        for algo in algos:
            if algo['name'] == self.algo_name:
                algo_exist = True
                break
        if not algo_exist:
            assert False
        assert self.file_manager.is_algo_exist_in_system(self.algo_name)

    def test_server_restart(self):
        # pre set -> remove all algorithms from system

        algos = self.controller.get_all_algorithms()
        for algo in algos:
            self.file_manager.remove_algo_system(algo['name'])
        algos = self.controller.get_all_algorithms()
        all_exist_in_system = True
        for algo in algos:
            all_exist_in_system = all_exist_in_system and self.file_manager.is_algo_exist_in_system(algo['name'])
        assert len(algos) > 0 and all_exist_in_system

    def test_add_algorithm_invalid_algo_type_case1(self):
        # case : algo type is not a list
        invalid_algo_type = "regressor"
        with self.assertRaises(TypeError):
            self.controller.add_new_algorithm(self.test_cf_content, self.algo_name,  TestUtils.get_dice_arg_list(), self.desc, self.addI,
                                              self.res_example, invalid_algo_type)

    def test_add_algorithm_invalid_algo_type_case2(self):
        # case : algo type is not a regressor
        invalid_algo_type = ["regression"]
        with self.assertRaises(ValueError):
            self.controller.add_new_algorithm(self.test_cf_content, self.algo_name, TestUtils.get_dice_arg_list(),
                                              self.desc, self.addI,
                                              self.res_example, invalid_algo_type)

    def test_add_algo_uppercase_algo_type(self):
        algo_type = ["REGRESSOR"]
        try:
            self.controller.add_new_algorithm(self.test_cf_content, self.algo_name, TestUtils.get_dice_arg_list(),
                                              self.desc, self.addI,
                                              self.res_example, algo_type)
            assert True
        except:
            assert False

    def test_add_algorithm_invalid_cf_arguments_case1(self):
        # case : 2 args with same name
        file_name = "DiCE_for_test"
        invalid_arg_desc = [{"param_name": "names", "description": "names for boys", "accepted_types": ["list"]},
                            {"param_name": "names", "description": "names for girls", "accepted_types": ["list"]}]
        self.file_manager = FileManager(TestConfig())
        test_cf_content = TestUtils.get_dice_content()
        cf_description = TestUtils.get_dice_cf_description()
        with self.assertRaises(ValueError):
            self.controller.add_new_algorithm(test_cf_content, file_name, invalid_arg_desc, self.desc, self.addI,
                                              self.res_example, self.algo_type)

    def test_add_algorithm_invalid_cf_arguments_case2(self):
        # case : arg with no name
        file_name = "DiCE_for_test"
        self.file_manager = FileManager(TestConfig())
        with open('additionals/' + file_name + '.py', 'r') as file:
            test_cf_content = file.read()
        invalid_arg_desc = [{"param_name": "", "description": "names for boys", "accepted_types": ["list"]},
                            {"param_name": "names", "description": "names for girls", "accepted_types": ["list"]}]
        with self.assertRaises(ValueError):
            self.controller.add_new_algorithm(test_cf_content, file_name, invalid_arg_desc, self.desc, self.addI,
                                              self.res_example, self.algo_type)

    def setUp(self) -> None:
        rand_num = random.randint(1, 10000)
        file_name = TestUtils.get_dice_algo_name()
        self.algo_name = file_name + '_' + str(rand_num)
        self.file_manager = FileManager(TestConfig())
        self.test_cf_content = TestUtils.get_dice_content()
        cf_description = TestUtils.get_dice_cf_description()
        self.cf_description = cf_description
        self.controller = AlgorithmsController(TestConfig())

        desc = "tell you what your age is"
        self.desc = desc
        addI = "additional"
        self.addI = addI
        res_example = ["25"]
        self.res_example = res_example
        self.algo_type = ["regressor"]

    def tearDown(self) -> None:
        self.file_manager.remove_algorithm(self.algo_name)
