import warnings
warnings.filterwarnings("ignore")
from keras.models import model_from_json
import pickle
import re
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import urllib.request
from string import punctuation
stop = set(stopwords.words('english'))
stop.update(list(punctuation))
lemmatizer = WordNetLemmatizer()


def load_model():
    #with urllib.request.urlopen("https://raw.githubusercontent.com/Mohnish226/data/master/msa_model_data/model.json") as json_file:
    with open('../model_data/model.json', 'r') as json_file:
        model = model_from_json(json_file.read())
    model.load_weights("../model_data/model.h5")
    #model.load_weights(urllib.request.urlopen('https://github.com/Mohnish226/data/blob/master/msa_model_data/model.h5?raw=true'))
    model._make_predict_function()
    #with urllib.request.urlopen('https://github.com/Mohnish226/data/blob/master/msa_model_data/tokenizer.pickle?raw=true') as file:
    with open('../model_data/tokenizer.pickle', 'rb') as file:
        token = pickle.load(file)
    return model, token


def text_clean(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+', '', text)
    text = " ".join(x for x in word_tokenize(str(text)) if x.strip().lower() not in stop)
    text = re.sub(r'\d+', '', text)
    text = " ".join(lemmatizer.lemmatize(x.lower()) for x in text.split())
    print(text)
    return(text)


def format_data(x, y=None, train=True, tokenizer=None,MAX_NB_WORDS=50000,MAX_SEQUENCE_LENGTH=300):
    if not tokenizer:
        tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~')
        tokenizer.fit_on_texts(x)
        print('Found %s unique tokens.' % len(tokenizer.word_index))
    x = tokenizer.texts_to_sequences(x)
    x = pad_sequences(x, maxlen=MAX_SEQUENCE_LENGTH)
    if not train:
        return x, tokenizer
    return x, y, tokenizer


def predict(text):
    try:
        print('data \n {} \n'.format(text))
        print('*'*10)
        model, tk = load_model()
        print('model loaded')
        text, tk = format_data(x=[text_clean(text)], train=False, tokenizer=tk)
        print('data formatted')
        print(model.predict(text)[0][0])
        return model.predict(text)[0][0]
    except Exception as e:
        print(print(text))
        print(e)
        return "Something went wrong"