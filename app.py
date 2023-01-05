from flask import Flask
from pymongo import MongoClient

from server.Tools.SystemConfig import SystemConfig
from server.serviceLayer import service

#setup mongodb
try:
    # uri = SystemConfig().MONGO_URI
    # cluster = MongoClient(uri)
    # SystemConfig().DB_CLUSTER = cluster
    # db = cluster["counterfactual"]
    # SystemConfig().DB = db
    print("connected to mongo")
except:
    print("cannot connect to mongo")

#setup flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "b294c388c2f58201ec96c43d60861de9ae357445"

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


app.register_blueprint(service.urls_blueprint)

if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(host='127.0.0.1', port=4000, debug=True)
    app.run()

    # print("hi")
