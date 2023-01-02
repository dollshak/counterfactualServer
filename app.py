import os
from flask import Flask
from pymongo import MongoClient
from server.serviceLayer import service

#setup mongodb
try:
    uri = os.environ.get('MONGO_URI')
    cluster = MongoClient(uri)
    db = cluster["counterfactual"]
    db2 = cluster["trying"]
except:
    print("cannot connect to mongo")

#setup flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "b294c388c2f58201ec96c43d60861de9ae357445"

@app.route("/users")
def create_user():
    try:
        user = {"name": "server", "lastname": "faraway"}
        db["users"].insert_one(user)
        return "suc"
    except:
        return("could not")


# app.register_blueprint(service.urls_blueprint)

if __name__ == "__main__":
    app.run(debug=True)



