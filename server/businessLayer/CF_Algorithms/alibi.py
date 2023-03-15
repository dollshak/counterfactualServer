import tensorflow
from alibi.explainers import Counterfactual

def initAlgo(model, arg_lst):
    shape = arg_lst['shape']
    target_proba = arg_lst['target_proba']
    tol = arg_lst['tol']  # want counterfactuals with p(class)>0.99
    target_class = arg_lst['target_class']  # any class other than 7 will do
    max_iter = arg_lst['max_iter']
    lam_init = arg_lst['lam_init']
    max_lam_steps = arg_lst['max_lam_steps']
    learning_rate_init = arg_lst['learning_rate_init']
    feature_range = arg_lst['feature_range']
    return Counterfactual(model, shape=shape, target_proba=target_proba, tol=tol,
                          target_class=target_class, max_iter=max_iter, lam_init=lam_init,
                          max_lam_steps=max_lam_steps, learning_rate_init=learning_rate_init,
                          feature_range=feature_range)