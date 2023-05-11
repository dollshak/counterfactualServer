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
    # uri = SystemConfig().MONGO_URI
    # cluster = MongoClient(uri)
    # SystemConfig().DB_CLUSTER = cluster
    # db = cluster["counterfactual"]
    # SystemConfig().DB = db
    tf.compat.v1.disable_eager_execution()
    print("connected to mongo")
    # d = {
    #     'shape': (1,) + (60000, 28, 28, 1)[1:],
    #     'target_proba': 1.0,
    #     'tol': 0.01,
    #     'target_class': 'other',
    #     'max_iter': 1000,
    #     'lam_init': 1e-1,
    #     'max_lam_steps': 10,
    #     'learning_rate_init': 0.1,
    #     'feature_range': (0, 255),
    # }
    #
    #
    # def cnn_model():
    #     x_in = Input(shape=(28, 28, 1))
    #     x = Conv2D(filters=64, kernel_size=2, padding='same', activation='relu')(x_in)
    #     x = MaxPooling2D(pool_size=2)(x)
    #     x = Dropout(0.3)(x)
    #
    #     x = Conv2D(filters=32, kernel_size=2, padding='same', activation='relu')(x)
    #     x = MaxPooling2D(pool_size=2)(x)
    #     x = Dropout(0.3)(x)
    #
    #     x = Flatten()(x)
    #     x = Dense(256, activation='relu')(x)
    #     x = Dropout(0.5)(x)
    #     x_out = Dense(10, activation='softmax')(x)
    #
    #     cnn = Model(inputs=x_in, outputs=x_out)
    #     cnn.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    #
    #     return cnn
    # cnn = cnn_model()
    # cf = initAlgo(cnn, d)
    # x = 3
except Exception as e:
    print("cannot connect to mongo")

# setup flask
app = Flask(__name__)
# CORS(app)
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
