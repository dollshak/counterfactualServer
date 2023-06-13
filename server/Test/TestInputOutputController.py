import unittest

from server.businessLayer.FileManager import FileManager
from server.businessLayer.Inputs_Handlers.InputOutputController import InputOutputController


class TestInputOutputController(unittest.TestCase):
    def test_handle_input_feature_list(self):
        feature_names, values = self.IOController.handle_input(self.input)
        self.assertEqual(feature_names, ['name', 'age', 'height', 'living area'])
        self.assertEqual(values, ['ido', 25, 183, 'rural'])

    def test_handle_output_feature_list(self):
        feature_names, values = self.IOController.handle_input(self.input)
        output = self.IOController.handle_output(feature_names, values, self.cf_results, self.algo_names,
                                                 self.model_result,self.algo_runtimes, 'FeatureList')
        self.assertEqual(output, self.expected_output)

    def test_handle_input_invalid_shape(self):
        wrong_input = [('name', 'ido'), ('age', 25), ('height', 183), ('living area', 'rural')]
        with self.assertRaises(TypeError):
            self.IOController.handle_input(wrong_input)

    def test_handle_output_no_output(self):
        cf_results = [[['ido', 27, 183, 'rural'], ['ido', 25, 189, 'rural']], []]
        feature_names, values = self.IOController.handle_input(self.input)
        output = self.IOController.handle_output(feature_names, values, cf_results, self.algo_names,self.model_result,self.algo_runtimes, 'FeatureList')
        self.assertEqual(['ido', 27, 183, 'rural'], output['output']['algo1']['results'][0])
        self.assertEqual(['ido', 25, 189, 'rural'], output['output']['algo1']['results'][1])
        self.assertEqual([], output['output']['algo2']['results'])

    def setUp(self) -> None:
        names = ['name','age','height','living area']
        values = ['ido',25,183,'rural']
        self.input = {'names':names,'values':values}
        self.model_result = [0.3]
        self.algo_runtimes = {'algo1': 3.2, 'algo2': 0.7}
        self.cf_results = [[['ido', 27, 183, 'rural'], ['ido', 25, 189, 'rural']],
                           [['ido', 30, 182, 'rural'], ['ido', 20, 199, 'rural']]]
        self.algo_names = ['algo1', 'algo2']
        self.expected_output = {
            'input':self.input,
            'output': {
                'algo1': {
                    'time': 3.2,
                    'results': [['ido', 27, 183, 'rural'], ['ido', 25, 189, 'rural']],
                    'errorMessage': ""},
                'algo2': {
                    'time': 0.7,
                    'results': [['ido', 30, 182, 'rural'], ['ido', 20, 199, 'rural']],
                    'errorMessage': ""}
            }
        }
        self.IOController = InputOutputController()

