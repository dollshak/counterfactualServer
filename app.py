import os
from flask import Flask
from pymongo import MongoClient
from server.serviceLayer import service

#setup mongodb
uri = os.environ.get('MONGO_URI')
cluster = MongoClient(uri)
db = cluster["counterfactual"]

#setup flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "b294c388c2f58201ec96c43d60861de9ae357445"

app.register_blueprint(service.urls_blueprint)

if __name__ == "__main__":
    app.run(debug=True)


