## preprocessing the data
import nltk
import contractions
import inflect
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from bs4 import BeautifulSoup
import re, string, unicodedata
from spellchecker import SpellChecker


###############################################################################

#code to download the required nltk modules data for the preprocessing pipeline
def nltk_preprocessing_required_downloads():
    nltk.download('omw-1.4', quiet=True)
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)

###############################################################################

#code to remove round brackets, double quotes, punctuation and white space from the data
def remove_round_brackets(data):
    return re.sub('\(.*?\)','',data)

def remove_double_quotes(data):
    return re.sub('[“”]','',data)

def remove_punc(data):
    trans = str.maketrans('','', string.punctuation)
    return data.translate(trans)

def white_space(data):
    return ' '.join(data.split())


def complete_noise(data):
    new_data = remove_round_brackets(data)
    new_data = remove_double_quotes(new_data)
    new_data = remove_punc(new_data)
    new_data = white_space(new_data)
    return new_data

###############################################################################

#code to convert the data to lower case, remove any contractions(e.g. don't -> do not), correct spellings of the data
def text_lower(data):
    return data.lower()

def contraction_replace(data):
    return contractions.fix(data)

spell = SpellChecker()
def correct_spellings(tokens):
    corrected_text = []
    misspelled_words = spell.unknown(tokens)
    for word in tokens:
        if word in misspelled_words:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
    return " ".join(corrected_text)


def normalization(data):
    text = text_lower(data)
    text = contraction_replace(text)
    tokens = nltk.word_tokenize(text)
    corrected_tokens = correct_spellings(tokens)
    return corrected_tokens

###############################################################################

#code to remove stopwords from the data, perform stemming or lemmatization on the data
def stopword(data):
    clean = []
    for i in data.split():
        if i not in stopwords.words('english'):
            clean.append(i)
    final_str = ""
    for i in clean:
        final_str += i + " "
    return final_str

def stemming(data):
    stemmer = LancasterStemmer()
    stemmed = []
    for i in data.split():
        stem = stemmer.stem(i)
        stemmed.append(stem)
    
    final_str = ""
    for i in stemmed:
        final_str += i + " "
    
    return final_str

def lemmatization(data):
    lemma = WordNetLemmatizer()
    lemmas = []
    for i in data.split():
        lem = lemma.lemmatize(i, pos='v')
        lemmas.append(lem)
    
    final_str = ""
    for i in lemmas:
        final_str += i + " "

    return final_str  


def final_process(data, additional_preprocessing):
    stopwords_removed = stopword(data)
    if additional_preprocessing.upper() == 'STEMMING':
        stemmed = stemming(stopwords_removed)
        return stemmed
    elif additional_preprocessing.upper() == 'LEMMATIZATION':
        lemm = lemmatization(stopwords_removed)
        return lemm
    else:
        return stopwords_removed

###############################################################################

#code to apply the preprocessing pipeline to the data and return the processed data
def preprocessing_pipeline(raw_data, additional_preprocessing=False):
    new_data = complete_noise(raw_data)
    new_data_norm = normalization(new_data)
    final_data = final_process(new_data_norm, additional_preprocessing)

    return final_data