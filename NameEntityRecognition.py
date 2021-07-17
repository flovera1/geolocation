import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

import spacy
from textblob import TextBlob
from pandas.core.common import flatten
from geotext import GeoText

nltk.download('brown', quiet=True)
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


nlp = spacy.load('en_core_web_sm')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class NameEntityRecognition:

    def __init__(self):
        self.list_of_entities = []

    def split_into_sentences(self, text):
        return nltk.sent_tokenize(text)

    def entity_recognition(self, sentence:str):
        sen = nlp(sentence)
        return list(sen.ents)

    def entity_recognition_text_blob(self, sentence: str):
        blob = TextBlob(sentence)
        return blob.noun_phrases

    def get_cities(self, sentence:str):
        places = GeoText(sentence)
        return places.cities

    def get_nouns(self, sentence: str):
        # create spacy
        doc = nlp(sentence)
        return_list = []
        for token in doc:
            # check token pos
            if token.pos_ == 'NOUN':
                # print token
                return_list.append(token.text)
        return return_list

    def get_interested_pos(self, sentence:str):
        list_of_entities = self.entity_recognition(sentence)
        list_of_nouns = self.get_nouns(sentence)

        return list_of_entities + list_of_nouns


def nlp_entities(sentence:str):
    doc = nlp(sentence)
    return_List = []
    for X in doc.ents:
        if X.label_ == 'GPE':
            return_List.append(X.text)
    return return_List


def get_entities_list(text):
    ner = NameEntityRecognition()
    list_of_entities = ner.get_interested_pos(text)
    return list_of_entities


def main():
    text = "The Statue of Liberty as seen from near Battery Park. #sandy #hurricanesandy"
    print(nlp_entities(text))
    # flat_list = get_entities_list(text)
    #
    # for i in flat_list:
    #     print(i)




if __name__ == "__main__":
    main()
