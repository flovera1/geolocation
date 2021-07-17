import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import SnowballStemmer
from bs4 import BeautifulSoup
from spellchecker import SpellChecker
import string
import re
import nltk
nltk.download('stopwords')


def load_dataframe(file:str):
    return pd.read_csv(file)

# Tokenizers
_tweetok = TweetTokenizer()
_wptok = WordPunctTokenizer()

# Stop Words
_stop_words = set(stopwords.words('english'))
_exclude = ["no"]
_stop_words = [w for w in _stop_words if not w in _exclude]

# Regular Expressions
_r1 = r'@[A-Za-z0-9_]+' # Twitter username
_r2 = r'http\S+|www\S+|[A-Za-z0-9\/.:]*\.com(\.[A-Za-z]+)*' # URLs
_r3 = r'#[A-Za-z0-9]+' # HashTags
_final_regex = r'|'.join((_r1, _r2, _r3)) # Final RegEx

# Spell Checker
_spell = SpellChecker(language='es')
_spell.word_frequency.load_words(['microsoft', 'apple', 'google','twitter', 'facebook', 'amazon', 'texting', 'nah'])

# Lemmatization
_lemmatizer = SnowballStemmer('english')

_df = pd.read_csv('~/Documents/geolocation/data/albertaT6.csv',
                  usecols=['id','user_screen_name','text','place_name','lon','lat'],
                  encoding = 'ISO-8859-1', low_memory=False)


def reduce_lengthening(text):
    pattern = re.compile(r"(.)\1{1,}")
    return pattern.sub(r"\1", text)


def preprocess_tweet(val_tweet):
    # HTML decoding
    val_tweet = BeautifulSoup(val_tweet, 'lxml').get_text()
    # Weird characters
    val_tweet = ''.join(filter(lambda x: x in string.printable, val_tweet))
    # # URLs, mentions and hashtags
    # valTweet = re.sub(_final_regex, '', valTweet)
    # To lowercase
    val_tweet = val_tweet.lower()
    # Only alpha characters
    val_tweet = re.sub(r'[^a-zA-Z]', ' ', val_tweet)
    # Typos correction
    v_tokens = _wptok.tokenize(val_tweet)
    v_tokens = [reduce_lengthening(w) for w in v_tokens]
    # Lonely letters removal
    v_tokens = [w for w in v_tokens if len(w) > 1]
    return v_tokens


def correct_spelling(val_tokens):
    # Discard null tweet
    if len(val_tokens) == 0:
        return ""
    # Long word check, discard tweet if there is a long word
    if len([w for w in val_tokens if len(w) > 40]) > 0:
        return ""
    # Misspelled words correction
    v_misspelled = _spell.unknown(val_tokens)
    if len(v_misspelled) > 0:
        val_tokens = [w if not w in v_misspelled else _spell.correction(w) for w in val_tokens]
        # Stop word drop
    val_tokens = [w for w in val_tokens if not w in _stop_words]
    return val_tokens


def lemmatize(val_tokens):
    return [_lemmatizer.stem(w) for w in val_tokens]


def remove_repeated(val_tokens):
    return ' '.join(sorted(set(val_tokens), key=val_tokens.index))

_texts = []
_ids = []
_lat = []
_lon = []
_to_tweet = len(_df['text'])
for i in range(0,_to_tweet):
    vTweet = preprocess_tweet(_df['text'][i])
    vTweet = correct_spelling(vTweet)
    vTweet = lemmatize(vTweet)
    vTweet = remove_repeated(vTweet)
    if vTweet != "":
        _texts.append(vTweet)
        _ids.append(_df['id'][i])
        _lat.append(_df['lat'][i])
        _lon.append(_df['lon'][i])
_cleaner_df = pd.DataFrame(_texts,columns=['text'])
_cleaner_df['id'] = _ids
_cleaner_df['lat'] = _lat
_cleaner_df['lon'] = _lon

_cleaner_df.to_csv('cooked_tweets_' + str(0) + '_' + str(_to_tweet) + '.csv', index = None, encoding='utf-8')