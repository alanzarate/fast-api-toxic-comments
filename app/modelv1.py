import pandas as pd
import numpy as np
import tensorflow as tf
import pickle
from keras.models import load_model
from tensorflow.keras.layers import TextVectorization

model = load_model('app/toxicityV2.h5')
from_disk = pickle.load(open('app/tv_layer_V2.pkl', 'rb'))
vectorizer = TextVectorization.from_config(from_disk['config'])
# You have to call `adapt` with some dummy data (BUG in Keras)
vectorizer.adapt(tf.data.Dataset.from_tensor_slices(["xyz"]))
vectorizer.set_weights(from_disk['weights'])

#input_text = vectorizer('vete a la mierda')
#res = model.predict(np.array([input_text]))
#res = model.predict(np.expand_dims(input_text, 0))
#res

class Predictor():
    def pred(self, newStr: str): 
        input_text = vectorizer(newStr)
        res = model.predict(np.expand_dims(input_text, 0)) 
        res = res.tolist()
        mapa = { "toxicity": res[0][0] ,
             "severe_toxic": res[0][1] ,
             "obscene": res[0][2] ,
             "threat": res[0][3] ,
             "insult": res[0][4] ,
             "identity_hate": res[0][5] }
        
        return mapa