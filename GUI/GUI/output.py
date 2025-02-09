from keras.models import load_model
import numpy as np
from keras import backend as K
from skimage.io import imread


def run(model_name, file_name):
    K.clear_session()
    model = load_model(model_name + ".h5")
    print("Compiling " + model_name)
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    print("Compiled")
    image = imread(file_name)
    print(image.shape)
    if not image.shape == (96,96,3):
        print("Image shape not proper")
        return 0
    imgB = np.stack(image, axis=0)
    img = np.expand_dims(imgB / 255.0, axis=0)
    print("Predicting")
    y_pred = model.predict(img)[0][0]
    print("Expected percentage:  " + str(y_pred * 100) + "%")
    return y_pred
