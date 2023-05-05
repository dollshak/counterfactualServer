import numpy as np
from numpy import random
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge


class ModelForTest:
    def __init__(self):
        self.length = np.array([])
        self.income_array = np.array([])
        self.outcome_array = np.array([])
        self.total_array = np.array([])
        self.loan_array = np.array([])
        self.generate_data()

        # sets data by model_type
        ######################################## REGRESSION ########################################
        self.result_reg = [
            self.get_res_reg(self.income_array[i], self.outcome_array[i], self.total_array[i], self.loan_array[i]) for i
            in
            range(self.length)]
        # create dataframe
        self.df_reg = pd.DataFrame(
            data={'income': self.income_array, 'outcome': self.outcome_array, 'total': self.total_array,
                  'loan': self.loan_array, 'label': self.result_reg})

        df_train_reg = self.df_reg.copy()
        df_train_reg = df_train_reg.drop('label', axis=1)
        x_data_reg = df_train_reg.to_numpy()
        y_data_reg = self.df_reg['label'].to_numpy()
        self.x_train_reg, self.x_val_reg, self.y_train_reg, self.y_val_reg = train_test_split(x_data_reg, y_data_reg,
                                                                                              test_size=0.2)
        ############################################################################################

        ######################################## CLASSIFICATION ########################################

        self.result_clf = [
            self.get_res_clf(self.income_array[i], self.outcome_array[i], self.total_array[i], self.loan_array[i]) for i
            in
            range(self.length)]

        self.df_clf = pd.DataFrame(
            data={'income': self.income_array, 'outcome': self.outcome_array, 'total': self.total_array,
                  'loan': self.loan_array, 'label': self.result_clf})

        df_train_clf = self.df_clf.copy()
        df_train_clf = df_train_clf.drop('label', axis=1)
        x_data_clf = df_train_clf.to_numpy()
        y_data_clf = self.df_clf['label'].to_numpy()
        self.x_train_clf, self.x_val_clf, self.y_train_clf, self.y_val_clf = train_test_split(x_data_clf, y_data_clf,
                                                                                              test_size=0.2)

        ############################################################################################

    def generate_data(self):
        self.length = 20000
        self.income_array = np.squeeze(random.randint(low=5000, high=20000, size=(1, self.length)))
        self.outcome_array = np.squeeze(random.randint(low=5000, high=10000, size=(1, self.length)))
        self.total_array = np.squeeze(random.randint(low=20000, high=100000, size=(1, self.length)))
        self.loan_array = np.squeeze(random.randint(low=50000, high=500000, size=(1, self.length)))

    def get_res_reg(self, income, outcome, total, loan):
        chance = ((income - outcome) * 6 + total) / loan
        return chance

    def get_res_clf(self, income, outcome, total, loan):
        chance = ((income - outcome) * 6 + total) / loan
        if chance < 0.3:
            return 0
        elif chance < 0.7:
            return 1
        else:
            return 2

    def get_regression_model(self):
        reg = Ridge(alpha=1.0).fit(self.x_train_reg, self.y_train_reg)
        return reg

    def get_clf_model(self):
        return LogisticRegression(solver='newton-cg').fit(self.x_val_clf, self.y_train_clf)

    def get_feature_names(self):
        return self.df_reg.columns[:-1]
