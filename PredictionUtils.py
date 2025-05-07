import pickle
import json
from tensorflow.keras.models import load_model
import os
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np



def preprocess_text(text_input):
    seq2int=[char2indx.get(c,0) for c in  text_input]
    padded_sequence=pad_sequences(np.array([seq2int]),maxlen=2000, padding='post', truncating='post')
    
    return padded_sequence


label_encoder=None
with open(os.path.join('LabelEncoder','label_encoder.pkl'),'rb') as file:
    label_encoder=pickle.load(file)
char2indx=None
with open(os.path.join('Vocabulary','char2idx.json'),'rb') as file:
    char2indx=json.load(file)
language_prediction_model=None
language_prediction_model=load_model(os.path.join('Model',"language_detection_model.h5"))




def predict_language(text_input):
    processed_input = preprocess_text(text_input)

    # Predict
    prediction = language_prediction_model.predict(processed_input)
    predicted_class_index = np.argmax(prediction)

    predicted_label=label_encoder.inverse_transform([predicted_class_index])[0]
    return predicted_label



