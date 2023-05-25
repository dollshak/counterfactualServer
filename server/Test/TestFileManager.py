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


    def test_is_algo_exist_case1(self):
        # case : exist in DB and in system
        self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        self.assertTrue(self.file_manager.is_algo_exist_in_db("DiCE_for_test"))
        self.file_manager.is_algo_exist_in_system("DiCE_for_test")

    def test_is_algo_exist_case2(self):
        # case : Algo exist only in DB - should create file in system
        self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        self.file_manager.remove_algo_system(self.cf_description.name)
        self.assertFalse(
            self.file_manager.is_algo_exist_in_system("DiCE_for_test"))  # should not be but needs to be created
        # self.assertTrue(self.file_manager.is_algo_exist_in_system("DiCE_for_test"))  # should be there now

    def test_is_algo_exist_case3(self):
        # case : Algo exist only in system -> remove it and return file does not exist.
        self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        self.file_manager.remove_from_db(self.cf_description.name)
        self.assertFalse(self.file_manager.is_algo_exist_in_db("DiCE_for_test"))

    def test_edit_algorithm_change_name(self):
        new_file_name = "Diff_name"
        self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        agd = [ArgumentDescription("age", "years old", [])]
        desc = "tell you what your age is"
        addI = "additional"
        res_example = ["25"]
        cf_description = CounterFactualAlgorithmDescription(new_file_name, agd, desc, addI, res_example, "regression")
        self.file_manager.edit_algorithm(self.test_cf_content, cf_description, self.file_name)
        self.assertTrue(self.file_manager.is_algo_exist_in_db("Diff_name"))

    # def test_edit_algorithm_change_content(self):
    #     assert False
    #
    # def test_edit_algorithm_change_arg_lst(self):
    #     assert False

    def test_edit_algorithm_change_description(self):
        self.file_manager = FileManager(TestConfig())
        self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        new_desc = "the goal is to tell you what your age is"
        new_cf_description = CounterFactualAlgorithmDescription(self.file_name, self.agd, new_desc, self.addI,
                                                                self.res_example, "regression")
        self.file_manager.edit_algorithm(self.test_cf_content, new_cf_description, self.file_name)
        alg: CounterFactualAlgorithmDescription = self.file_manager.get_algorithm(
            self.file_name)  # TODO check if type is correct
        self.assertEqual(alg['description'], "the goal is to tell you what your age is")

    def test_edit_algorithm_change_additional_info(self):
        self.file_manager = FileManager(TestConfig())
        self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        new_add_info = "even more additional"
        new_cf_description = CounterFactualAlgorithmDescription(self.file_name, self.agd, self.desc, new_add_info,
                                                                self.res_example, "regression")
        self.file_manager.edit_algorithm(self.test_cf_content, new_cf_description, self.file_name)
        alg: CounterFactualAlgorithmDescription = self.file_manager.get_algorithm(
            self.file_name)
        self.assertEqual(alg['additional_info'], "even more additional")

    def test_edit_algorithm_empty_output_example(self):
        # case :list of  empty string
        self.file_manager = FileManager(TestConfig())
        self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        new_example_output = [""]
        new_cf_description = CounterFactualAlgorithmDescription(self.file_name, self.agd, self.desc, self.addI,
                                                                new_example_output, "regression")
        self.assertRaises(Exception,
                          self.file_manager.edit_algorithm(self.test_cf_content, new_cf_description, self.file_name))

    def test_edit_algorithm_change_output_type(self):
        self.file_manager = FileManager(TestConfig())
        self.file_manager.add_algorithm(self.test_cf_content, self.cf_description)
        new_example_output = ["text not number"]
        new_cf_description = CounterFactualAlgorithmDescription(self.file_name, self.agd, self.desc, self.addI,
                                                                new_example_output, "regression")
        self.file_manager.edit_algorithm(self.test_cf_content, new_cf_description, self.file_name)
        alg: CounterFactualAlgorithmDescription = self.file_manager.get_algorithm(
            self.file_name)
        self.assertTrue(isinstance(alg['output_example'],list))  # Checking that list
        for item in alg['output_example']:
            self.assertTrue(isinstance(item,str))  # Checking that each element is string

    def setUp(self) -> None:
        file_name = 'DiCE_for_test'
        self.file_name = file_name
        self.file_manager = FileManager(TestConfig())
        with open('additionals/' + file_name + '.py', 'r') as file:
            self.test_cf_content = file.read()
        agd = [ArgumentDescription("age", "years old", [])]
        self.agd = agd
        desc = "tell you what your age is"
        self.desc = desc
        addI = "additional"
        self.addI = addI
        res_example = ["25"]
        self.res_example = res_example
        cf_description = CounterFactualAlgorithmDescription(file_name, agd, desc, addI, res_example, ["regressor"])
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
