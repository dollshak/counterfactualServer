import unittest
import sklearn
from sklearn.linear_model import LinearRegression

from server.businessLayer.Inputs_Handlers.PickleModel import PickleModel
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import os


class TestPickle(unittest.TestCase):
    def test_to_pickle(self):
        directory = os.getcwd()
        filename = 'testToPickle'
        self.remove_file_if_exist(directory, filename)
        PickleModel.to_pickle_file(self.model, "%s" % filename, directory=directory)
        files = os.listdir(directory)
        self.assertIn(('%s.pkl' % filename), files)
        self.remove_file_if_exist(directory, filename)

    def test_from_pickle(self):
        directory = os.getcwd()
        filename = 'testToPickle'
        self.remove_file_if_exist(directory, filename)
        PickleModel.to_pickle_file(self.model, "%s" % filename, directory=directory)
        path = f'{directory}/{filename}.pkl'
        from_pickle_model = PickleModel.from_pickle_file(path)
        self.assertEqual(from_pickle_model.score(self.x_text, self.y_test), self.model.score(self.x_text, self.y_test))
        self.remove_file_if_exist(directory, filename)

    def remove_file_if_exist(self, directory, filename):
        files = os.listdir(directory)
        if ('%s.pkl' % filename) in files:
            os.remove(f'{directory}/{filename}.pkl')

    def setUp(self) -> None:
        self.get_regression_model()

    def get_regression_model(self):
        x, y = make_regression()
        x_train, self.x_text, y_train, self.y_test = train_test_split(x, y, test_size=0.2)
        self.model = LinearRegression()
        self.model.fit(x_train, y_train)
