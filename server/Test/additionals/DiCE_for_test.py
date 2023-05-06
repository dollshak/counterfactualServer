import dice_ml
from dice_ml.utils import helpers  # helper functions
from sklearn.model_selection import train_test_split
import pandas as pd
import json


def initAlgo(model, arg_lst, data=None):
    return DiCE_for_test(arg_lst, model)


class DiCE_for_test:
    """
    :param cf_args: dictionary contains keys:
                <p>
                model_type :  'regressor' or 'classifier'
                <p>
                <p>
                features :  dictionary: <feature name , array[min value, max value]>
                e.g: 'income' : [1000,2000]
                <p>
                <p>
                outcome_name: string of target column name
                <p>

    """

    def __init__(self, cf_args, model, data=None):
        # extract arguments
        features = cf_args['features']
        outcome_name = cf_args['outcome_name']
        self.feature_names = features.keys()
        self.total_CFs = cf_args['total_CFs']
        self.desired_class = cf_args['desired_class']
        self.desired_range = cf_args['desired_range']
        self.model_type = 'classifier' if cf_args['is_classifier'] else 'regressor'
        # create explainer
        d = dice_ml.data.Data(features=features, outcome_name=outcome_name)
        self.m = dice_ml.Model(model=model, backend='sklearn', model_type=self.model_type)
        self.exp = dice_ml.Dice(d, self.m)

    def explain(self, model_input):
        data = {}
        if len(model_input) < len(self.feature_names):
            raise Exception(f'inputs length {len(model_input)} is smaller than expected {len(self.feature_names)}')
        for index, feature_name in enumerate(self.feature_names):
            data[feature_name] = [model_input[index]]
        df = pd.DataFrame(data=data)
        if self.model_type == "classifier":
            dice_exp = self.exp.generate_counterfactuals(df, self.total_CFs, self.desired_class)
        else:
            dice_exp = self.exp.generate_counterfactuals(df, self.total_CFs, desired_range=self.desired_range)
        json_result = dice_exp.to_json()
        json_data = json.loads(json_result)
        results = json_data['cfs_list'][0]
        return results
