import numpy as np
from keras.preprocessing import image
from keras.models import load_model



def predict(path):
    model=load_model('clothWeights.h5')
    file = path

    img = image.load_img(file, target_size=(140, 140))

    img = image.img_to_array(img)

    img = np.expand_dims(img, axis=0)
    img = img/255
    prediction_prob = model.predict_classes(img)
    
    return prediction_prob