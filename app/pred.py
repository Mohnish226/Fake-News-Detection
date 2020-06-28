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
from string import punctuation
stop = set(stopwords.words('english'))
stop.update(list(punctuation))
lemmatizer = WordNetLemmatizer()


def load_model():
    with open('../model_data/model.json', 'r') as json_file:
        model = model_from_json(json_file.read())
    model.load_weights("../model_data/model.h5")
    model._make_predict_function()
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

predict('''
Loyalty matters to Donald Trump! Alabama Senator Jeff Sessions has been beside Donald Trump since day one. He spoke out against Paul Ryan in June regarding Ryan’s lack of support for Trump:Sen. Jefferson Beauregard Sessions III, Donald Trump’s friendly but fierce Alabama ally, has a message for Republicans still queasy about their party’s nominee: Tide’s about to roll over you.Sessions, a 69-year-old former state attorney general who famously donned the “Make America Great Again” trucker’s cap at a massive rally in Mobile last August, thinks Trump is more a movement than a man. And this sprightly son of country preachers and teachers is on a mission to evangelize maybe-Trumpers like House Speaker Paul Ryan on the Gospel According to Donald — with a sermon on self-preservation. “My advice is to listen and accept the will of the American people, the Republican voters — the Republican Party is the Republican voters,” he added — a pointed reference to Ryan’s suggestion that he, and not the presumptive party nominee, represents authentic conservative values. “Give me a break! A lot of our drift within our party has gotten away from the will of the voters. … I think the leaders in all parties tend to adjust to reality. They just have to or they won’t remain in office. … Already many are sensing it.” Via: PoliticoHe’s now been offered and has accepted the cabinet position of Attorney General in the Trump administration.One of the key things about Senator Sessions that’s most important to note is that he’s been a lone soldier in the fight against illegal immigration and refugee resettlement. It looks like Donald Trump is serious when he said he would put Americans first.We couldn’t be happier!The battle on this has been ignored by pretty much all of the Congress for way too long. Our hope is that Senator Sessions will work quickly to stop the flow of illegals across our border and to take a hard look at the refugee resettlement program to defund it. Great choice!FOX News reported:Alabama Sen. Jeff Sessions, who jumped aboard the Donald Trump train long before the real estate mogul sewed up the Republican nomination, has been offered the post of attorney general, Fox News has confirmed.Sessions, 69, who advised Trump on immigration during the bruising campaign, was U.S. attorney for the Southern District of Alabama from 1981 to 1993 before being elected to the U.S. Senate in 1996. He was re-elected to a fourth term in 2014.Trending: CHAZ Shooting Victim Wants to Sue Police for Not Showing Up to the “Autonomous Zone”Sessions was famously photographed in a “Make America Great Again” baseball cap at an August, 2015 Trump rally, and formally endorsed Trump on Feb. 28, 2016. His longtime spokesman, Stephen Miller, later joined the Trump campaign as a senior adviser.
''')