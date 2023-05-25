import numpy as np

import scipy

from scipy.optimize import minimize

import random


def initAlgo(model, arg_lst, data=None):
    MADs = arg_lst["features_medians"]

    f = model.predict

    learning_rate = 0.1

    ytag = arg_lst["ytag"]

    epsilon = 0.1

    Lambda = 1

    ranges = arg_lst["features_ranges"]

    max_iter = 300

    wac = wachter_et_al(MADs, f, ytag, epsilon, Lambda, learning_rate, max_iter, ranges)

    return wac


class wachter_et_al:

    def __init__(self, MADs, f, ytag, epsilon, Lambda, learning_rate, max_iter, ranges):

        self.max_iter = max_iter

        self.ytag = ytag

        self.epsilon = epsilon

        self.f = f

        self.MADs = MADs

        self.learning_rate = learning_rate

        self.Lambda = Lambda

        self.ranges = ranges

    def _dist(self, x, xtag):

        sigma = 0

        p = len(x)

        for i in range(p):
            MADj = self.MADs[i]

            sigma = sigma + np.abs(x[i] - xtag[i]) / MADj

        return sigma

    def _L(self, xtag):

        return self.Lambda * (self.f(np.array([xtag]))[0] - self.ytag) ** 2 + self._dist(self.x, xtag)

    def explain(self, x):

        self.x = x

        cfslst = list()

        xtag = np.empty(len(x))

        iter = 0

        while iter < 5:

            for i in range(len(x)):
                xtag[i] = random.randrange(self.ranges[i][0], self.ranges[i][1])

            res = self._find_CF(xtag)

            cfslst.append(res)

            iter = iter + 1

        return cfslst

    def _find_CF(self, xtag):

        xtag = minimize(self._L, xtag).x

        iter = 1

        while iter < self.max_iter and np.abs(self.f(np.array([xtag])) - self.ytag) > self.epsilon:
            self.Lambda = self.Lambda + self.learning_rate

            xtag = minimize(self._L, xtag).x

            iter = iter + 1

        return np.append(xtag, self.f(np.array([xtag]))).tolist()
