#1
import tensorflow as tf
tf.get_logger().setLevel(40) # suppress deprecation messages
tf.compat.v1.disable_v2_behavior()
from tensorflow import keras
from keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPooling2D, Input
from keras.models import Model, load_model
from keras.utils import to_categorical
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from time import time
import alibi_temp
# from alibi.explainers import Counterfactual

def run():
    #2
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    print('x_train shape:', x_train.shape, 'y_train shape:', y_train.shape)
    plt.gray()
    plt.imshow(x_test[1]);

    #3
    x_train = x_train.astype('float32') / 255
    x_test = x_test.astype('float32') / 255
    x_train = np.reshape(x_train, x_train.shape + (1,))
    x_test = np.reshape(x_test, x_test.shape + (1,))
    print('x_train shape:', x_train.shape, 'x_test shape:', x_test.shape)
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    print('y_train shape:', y_train.shape, 'y_test shape:', y_test.shape)

    #4
    xmin, xmax = -.5, .5
    x_train = ((x_train - x_train.min()) / (x_train.max() - x_train.min())) * (xmax - xmin) + xmin
    x_test = ((x_test - x_test.min()) / (x_test.max() - x_test.min())) * (xmax - xmin) + xmin

    #5
    def cnn_model():
        x_in = Input(shape=(28, 28, 1))
        x = Conv2D(filters=64, kernel_size=2, padding='same', activation='relu')(x_in)
        x = MaxPooling2D(pool_size=2)(x)
        x = Dropout(0.3)(x)

        x = Conv2D(filters=32, kernel_size=2, padding='same', activation='relu')(x)
        x = MaxPooling2D(pool_size=2)(x)
        x = Dropout(0.3)(x)

        x = Flatten()(x)
        x = Dense(256, activation='relu')(x)
        x = Dropout(0.5)(x)
        x_out = Dense(10, activation='softmax')(x)

        cnn = Model(inputs=x_in, outputs=x_out)
        cnn.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        return cnn

    cnn = cnn_model()
    cnn.evaluate(x_test, y_test, verbose=0)

    #6
    cnn = cnn_model()
    cnn.summary()
    cnn.fit(x_train, y_train, batch_size=64, epochs=3, verbose=0)
    cnn.save('mnist_cnn.h5')

    #7
    cnn = load_model('mnist_cnn.h5')
    score = cnn.evaluate(x_test, y_test, verbose=0)
    print('Test accuracy: ', score[1])

    #8
    X = x_test[0].reshape((1,) + x_test[0].shape)
    plt.imshow(X.reshape(28, 28));

    #9
    shape = (1,) + x_train.shape[1:]
    target_proba = 1.0
    tol = 0.01 # want counterfactuals with p(class)>0.99
    target_class = 'other' # any class other than 7 will do
    max_iter = 1000
    lam_init = 1e-1
    max_lam_steps = 10
    learning_rate_init = 0.1
    feature_range = (x_train.min(),x_train.max())

    #10
    cf = Counterfactual(cnn, shape=shape, target_proba=target_proba, tol=tol,
                        target_class=target_class, max_iter=max_iter, lam_init=lam_init,
                        max_lam_steps=max_lam_steps, learning_rate_init=learning_rate_init,
                        feature_range=feature_range)

    start_time = time()
    explanation = cf.explain(X)
    print('Explanation took {:.3f} sec'.format(time() - start_time))

    #11
    pred_class = explanation.cf['class']
    proba = explanation.cf['proba'][0][pred_class]

    print(f'Counterfactual prediction: {pred_class} with probability {proba}')
    plt.imshow(explanation.cf['X'].reshape(28, 28));

