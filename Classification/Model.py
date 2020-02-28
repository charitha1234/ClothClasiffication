import numpy as np
from keras.preprocessing import image
from keras.models import load_model



def predict(path):
    class1=""
    class2=""
    model=load_model('clothWeights.h5')
    file = path

    img = image.load_img(file, target_size=(140, 140))

    img = image.img_to_array(img)

    img = np.expand_dims(img, axis=0)
    img = img/255
    prediction_prob = model.predict_classes(img)
    patterns=['irregular','solid','plaid','striped']


    class1=patterns[prediction_prob.tolist()[0]]

    if(prediction_prob.tolist()[0]==0):
        model=load_model('IrregularWeights.h5')
        img = image.load_img(file, target_size=(140, 140))

        img = image.img_to_array(img)

        img = np.expand_dims(img, axis=0)
        img = img/255
        prediction_prob = model.predict_classes(img)
        patterns=['polka dot','floral']
        class2=patterns[prediction_prob.tolist()[0]]
    return class1,class2