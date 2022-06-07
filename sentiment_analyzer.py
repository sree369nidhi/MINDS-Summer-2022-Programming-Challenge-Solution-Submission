##sentiment analysis
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import operator
import pandas as pd
import numpy as np
import re

###############################################################################

# code to download the vader lexicon data from nltk
def sentiment_analysis_required_downloads():
    nltk.download('vader_lexicon', quiet=True)

###############################################################################

# code for nltk sentiment analysis using vader lexicon and to extract the sentiment score (float between -1 to 1) and the sentiment
def nltk_sentiment_analyzer(df, column):
    sia = SentimentIntensityAnalyzer()
    df["nltk_sentiment_score"] = df[column].apply(lambda x: sia.polarity_scores(x)["compound"])
    df["nltk_sentiment"] = np.select([df["nltk_sentiment_score"] < 0, df["nltk_sentiment_score"] == 0, df["nltk_sentiment_score"] > 0], ['neg', 'neu', 'pos'])

###############################################################################

# code for textblob sentiment analysis and to extract the sentiment score (float between -1 to 1) and the sentiment
def textblob_sentiment_analyzer(df, column):
    df["textblob_sentiment_score"] = df[column].apply(lambda x: TextBlob(x).sentiment.polarity)
    df["textblob_sentiment"] = np.select([df["textblob_sentiment_score"] < 0, df["textblob_sentiment_score"] == 0, df["textblob_sentiment_score"] > 0], ['neg', 'neu', 'pos'])

###############################################################################

# code to perform the sentiment analysis on the dataframe given the column
def sentiment_analyzer(df, column, kind='NLTK_VADER'):
    if kind == 'NLTK_VADER':
        nltk_sentiment_analyzer(df, column)
    elif kind == 'TEXTBLOB':
        textblob_sentiment_analyzer(df, column)

###############################################################################