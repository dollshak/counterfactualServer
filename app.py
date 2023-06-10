import sklearn.linear_model
from flask import Flask
# from flask_cors import CORS
from pymongo import MongoClient
import tensorflow as tf
from server.Tools.SystemConfig import SystemConfig
from server.serviceLayer import service
from sklearn.linear_model import LogisticRegression
from keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPooling2D, Input
from keras.models import Model, load_model

# setup mongodb
try:
    tf.compat.v1.disable_eager_execution()
    print("connected to mongo")

except Exception as e:
    print("cannot connect to mongo")

# setup flask
app = Flask(__name__)
# CORS(app)
app.config["SECRET_KEY"] = "b294c388c2f58201ec96c43d60861de9ae357445"



app.register_blueprint(service.urls_blueprint)

if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(host='127.0.0.1', port=4000, debug=True)
    app.run()

