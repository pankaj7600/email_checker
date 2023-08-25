import streamlit as st 
import pickle
import pandas as pd

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string


tfidf = pickle.load(open('vector.pkl','rb'))
model= pickle.load(open('model.pkl','rb'))


nltk.download('punkt')
nltk.download('stopwords')

def lowercase_text(text):
    return text.lower()

def tokenize_text(text):
    return nltk.word_tokenize(text)

def remove_special_characters(tokens):
    return [token for token in tokens if token.isalnum()] #alphanumeric

def remove_stopwords_and_punctuation(tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words and token not in string.punctuation]

def stem_tokens(tokens):
    ps = PorterStemmer()
    return [ps.stem(token) for token in tokens]

def transform_text(text):
    text = lowercase_text(text)
    tokens = tokenize_text(text)
    tokens = remove_special_characters(tokens)
    tokens = remove_stopwords_and_punctuation(tokens)
    tokens = stem_tokens(tokens)
    return " ".join(tokens)


st.title('Emails/sms Spam Classfier')
input_sms=st.text_area('enter the message')
if st.button('prediction'):
    transformed_sms=transform_text(input_sms)
    vector_input=tfidf.transform([transformed_sms])

    result=model.predict(vector_input)[0]
    if result==1:
        st.header('spam')
    else:
        st.header('not spam')