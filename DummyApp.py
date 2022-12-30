from server.businessLayer.CF_Algorithms.Dummy_CF import Dummy_CF
from server.businessLayer.MlModel import MlModel


def dummy_predict(x):
    income = x[0]
    total = x[1]
    loan = x[2]
    ratio = (income * 6 + total) / loan
    return min(ratio, 1)


def create_dummy_model():
    # dummy_loan_model = {'fit': lambda income, total, loan: loan < (income * 6 + total)}
    dummy_loan_model = MlModel()
    dummy_loan_model.predict = lambda x: dummy_predict(x)
    return dummy_loan_model
    # return lambda income, total, loan: loan < (income * 6 + total)


if __name__ == "__main__":
    model = create_dummy_model()
    cf = Dummy_CF("dummy", None, list(), model)
    arg1 = [6000, 10000, 2000000]
    print(model.predict(arg1))
    explain = cf.explain(arg1)
    print(explain)
    print(model.predict(explain))
    # arg2 = [6000, 10000, 20000]
    # print(model.predict(arg2))
