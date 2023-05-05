import unittest

from server.businessLayer.Inputs_Handlers.InputOutputController import InputOutputController


class TestInputOutputController(unittest.TestCase):
    def test_handle_input_feature_list(self):
        io_controller = InputOutputController()
        feature_names, values = io_controller.handle_input(self.input)
        self.assertEqual(feature_names, ['name', 'age', 'height', 'living area'])
        self.assertEqual(values, ['ido', 25, 183, 'rural'])

    def test_handle_output_feature_list(self):
        io_controller = InputOutputController()
        feature_names, values = io_controller.handle_input(self.input)
        output = io_controller.handle_output(feature_names, values ,self.cf_results, self.algo_names, 'FeatureList')
        self.assertEqual(output, self.expected_output)

    def setUp(self) -> None:
        self.input = {
            'name': 'ido',
            'age': 25,
            'height': 183,
            'living area': 'rural'
        }
        self.cf_results = [[['ido', 27, 183, 'rural'], ['ido', 25, 189, 'rural']],
                           [['ido', 30, 182, 'rural'], ['ido', 20, 199, 'rural']]]
        self.algo_names = ['test1', 'test2']
        self.expected_output = {
            'input': {
                'name': 'ido',
                'age': 25,
                'height': 183,
                'living area': 'rural'
            },
            'output': {
                'test1': [['ido', 27, 183, 'rural'], ['ido', 25, 189, 'rural']],
                'test2': [['ido', 30, 182, 'rural'], ['ido', 20, 199, 'rural']]
            }
        }
