import os
from flask import Flask
from pymongo import MongoClient

from server.businessLayer.LinearRegression import LinearRegression
from server.serviceLayer import service
import alibi

#setup mongodb
# try:
#     # uri = os.environ.get('MONGO_URI')
#     uri = "mongodb+srv://Shaked:123@counterfactualdb.wejhesh.mongodb.net/?retryWrites=true&w=majority"
#     cluster = MongoClient(uri)
#     print("connected to mongo")
#     # db = cluster["counterfactual"]
# except:
#     print("cannot connect to mongo")

# #setup flask
# app = Flask(__name__)
# app.config["SECRET_KEY"] = "b294c388c2f58201ec96c43d60861de9ae357445"
#
# @app.route("/users")
# def create_user():
#     try:
#         db = cluster["counterfactual"]
#         print("reached db")
#         user = {"name": "server", "lastname": "faraway"}
#         db["users"].insert_one(user)
#         return "suc"
#     except Exception as e: print(e)
#
# @app.route("/")
# def index():
#     return "helo"


# app.register_blueprint(service.urls_blueprint)

if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(host='127.0.0.1', port=4000, debug=True)
    # app.run()
    LR = LinearRegression()
    model = LR.model

    # print("hi")
    print(model)

