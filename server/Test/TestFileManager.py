import random
import unittest

from server.Test.additionals.TestConfig import TestConfig
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.FileManager import FileManager


class TestFileManager(unittest.TestCase):
    def test_add_remove_algo(self):
        #  remove if algo is already exist
        self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        self.assertTrue(self.file_manager.is_algo_exist_in_db(self.file_name), "didn't manage to save the algo in db")
        self.assertTrue(self.file_manager.is_algo_exist_in_system(self.file_name),
                        "didn't manage to save the algo in the system")

    def test_add_existing_algo(self):
        self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        if not self.is_algo_exist_anywhere(self.file_name):
            self.assertFalse(True, "didn't manage to save the algo")
        try:
            self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
            assert False
        except FileExistsError:
            assert True
        except:
            assert False

    def test_get_all_algorithms(self):
        #         TODO need to fix here -> input changed


        # create random inorder to promise does not find the previous file
        randText = str(random.randint(1, 10000))
        second_algo_name = self.file_name + randText
        # add algo1
        self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        # add algo2
        cf_description_2 = CounterFactualAlgorithmDescription(second_algo_name, self.cf_description.argument_lst,
                                                              self.cf_description.description,
                                                              self.cf_description.additional_info,
                                                              self.cf_description.output_example,
                                                              "regression")
        self.file_manager.add_algorithm(self.test_cf_content, cf_description_2)
        if self.file_manager.is_algo_exist_in_system(second_algo_name) and self.file_manager.is_algo_exist_in_system(
                self.file_name):
            self.file_manager.remove_algo(second_algo_name)
            assert True

    def test_unhandled_file_type(self):
        # TODO implement here and in code -> receive file with unknown type as counter factual (validate informative message too)
        assert False

    def test_add_invalid_cf_arguments(self):
        # TODO test if the arguments is invalid -> by that i mean for example:
        #  has no name
        # 2 same names
        # no example gained

        assert False

    def test_is_algo_exist(self):
        #     TODO split this text to 3 different tests sa following
        #      TODO tests:
        #       if file exist in db return true
        #       if file only in db -> create file in system too
        #       if file only in system -> remove it. and return file does not exist
        #
        assert False

    def test_edit_algorith(self):
        # TODO need to split to many tests:
        # 1. change name
        # 2. change content
        # 3. arg_lst
        # 4. description
        # 5. additional info
        # 6. output example
        # 7. output type
        # in all of the above, check changed in db
        assert False

    def setUp(self) -> None:
        file_name = 'DiCE_for_test'
        self.file_name = file_name
        self.file_manager = FileManager(TestConfig())
        with open('additionals/' + file_name + '.py', 'r') as file:
            self.test_cf_content = file.read()
        agd = [ArgumentDescription("age", "years old", [], {})]
        self.agd = agd
        desc = "tell you what your age is"
        self.desc = desc
        addI = "additional"
        self.addI = addI
        res_example = ["25"]
        self.res_example = res_example
        cf_description = CounterFactualAlgorithmDescription(file_name, agd, desc, addI, res_example, "regression")
        self.cf_description = cf_description

        if self.is_algo_exist_anywhere(self.file_name):
            self.file_manager.remove_algo(self.file_name)
        # if remove fails -> assert false
        if self.is_algo_exist_anywhere(self.file_name):
            assert False

    def is_algo_exist_anywhere(self, file_name):
        return self.file_manager.is_algo_exist_in_db(file_name) or self.file_manager.is_algo_exist_in_system(
            file_name)

    def tearDown(self) -> None:
        self.file_manager.remove_algo('DiCE_for_test')
