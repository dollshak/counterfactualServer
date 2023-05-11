import unittest
import random

from pandocfilters import Math

from server.Test.additionals.TestConfig import TestConfig
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.AlgorithmsController import AlgorithmsController
from server.businessLayer.FileManager import FileManager


class TestAlgorithmController(unittest.TestCase):

    def test_restore_algorithm(self):
        # setting start position -> algo in db but not in system
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

    def setUp(self) -> None:
        rand_num = random.randint(1, 10000)
        file_name = 'DiCE_for_test'
        self.algo_name = file_name + '_' + str(rand_num)
        self.file_manager = FileManager(TestConfig())
        with open('additionals/' + file_name + '.py', 'r') as file:
            self.test_cf_content = file.read()
        agd = [ArgumentDescription("age", "years old", ["str"])]
        self.agd = agd
        desc = "tell you what your age is"
        self.desc = desc
        addI = "additional"
        self.addI = addI
        res_example = ["25"]
        self.res_example = res_example
        cf_description = CounterFactualAlgorithmDescription(self.algo_name, agd, desc, addI, res_example, "regression")
        self.cf_description = cf_description

        self.controller = AlgorithmsController(TestConfig())
