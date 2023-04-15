import dice_ml
from dice_ml.utils import helpers  # helper functions
from sklearn.model_selection import train_test_split


def initAlgo(model, arg_lst, data=None):
    if data is None:
        raise Exception("Tried to init DiCE with no data.")
    return DiCE_dup(data, model, arg_lst)


class DiCE_dup:

    def __init__(self, cf_args: list, model, data=None):
        self.exp = dice_ml.Dice(data, model)
        self.total_CFs = cf_args['total_CFs']
        self.desired_class = cf_args['desired_class']

    def explain(self, model_input):
        dice_exp = self.exp.generate_counterfactuals(model_input, self.total_CFs, self.desired_class)
        return dice_exp.visualize_as_dataframe()
