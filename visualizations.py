##visualizing the data
import pandas as pd
import textblob
import plotly as plt
import plotly.express as px


def make_visualizations(news_df):

    df = news_df

    ###############################################################################

    # Histogram of Sentiment Polarity (categories) Distribution for the News Articles
    fig = px.histogram(df, x="nltk_sentiment", color="nltk_sentiment", title='Histogram of Sentiment Polarity Distribution')
    fig.update_layout(font_color="black", font=dict(size=13,), autosize=False, width=900, height=700)

    fig.write_image("Histogram of Sentiment Polarity (categories) Distribution.png", scale=2.1934758155230596)

    ###############################################################################

    # Boxplot of Sentiment Polarity (scores) for the News Articles
    fig = px.box(df, x="nltk_sentiment_score", title='Sentiment Polarity Box plot')
    fig.update_layout(font_color="black", font=dict(size=13,), autosize=False, width=900, height=700)

    fig.write_image("Sentiment Polarity Box plot.png", scale=2.1934758155230596)

    ###############################################################################

    # Length of the text (count of words in Thousands) for the News Articles
    df['len'] = df['Preprocessed_Text_Content'].str.len()

    fig = px.histogram(df, x="len", title='Length of the text (count of words in Thousands).')
    fig.update_layout(font_color="black", font=dict(size=13,), autosize=False, width=900, height=700)
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                    marker_line_width=0.9, opacity=0.6)

    fig.write_image("Length of the text (count of words in Thousands).png", scale=2.1934758155230596)

    ###############################################################################

    # Top 20 words in the News Articles before removing stop words
    all_unprocessed_articles = df['Text_Content'].to_list()
    all_unprocessed_articles.pop(6)

    from sklearn.feature_extraction.text import CountVectorizer

    def get_top_n_words(corpus, n=None):
        vec = CountVectorizer().fit(corpus)
        bag_of_words = vec.transform(corpus)
        sum_words = bag_of_words.sum(axis=0) 
        words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
        words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
        return words_freq[:n]


    common_words = get_top_n_words(all_unprocessed_articles, 20)

    df1 = pd.DataFrame(common_words, columns = ['Review Text' , 'count'])
    raw_top20words = df1.groupby('Review Text').sum()['count'].sort_values(ascending=False)

    fig = px.bar(raw_top20words, x=raw_top20words.index, y="count", title='Top 20 words in the News Articles before removing stop words')
    fig.update_traces(marker_color='gold', marker_line_color='rgb(8,48,107)',
                    marker_line_width=0.9, opacity=0.6)

    fig.write_image("Top 20 words in the News Articles before removing stop words.png", scale=2.1934758155230596)

    ###############################################################################

    # Top 20 words in the News Articles after removing stop words
    all_processed_articles = df['Preprocessed_Text_Content'].to_list()
    all_processed_articles.pop(6)

    common_words = get_top_n_words(all_processed_articles, 20)

    df1 = pd.DataFrame(common_words, columns = ['Review Text' , 'count'])
    top20words = df1.groupby('Review Text').sum()['count'].sort_values(ascending=False)

    fig = px.bar(top20words, x=top20words.index, y="count", title='Top 20 words in the News Articles after removing stop words')
    fig.update_traces(marker_color='gold', marker_line_color='rgb(8,48,107)',
                    marker_line_width=0.9, opacity=0.6)

    fig.write_image("Top 20 words in the News Articles after removing stop words.png", scale=2.1934758155230596)

    ###############################################################################

    # Top 20 Bigram words in the News Articles before removing stop words
    def get_top_n_bigram(corpus, n=None):
        vec = CountVectorizer(ngram_range=(2, 2)).fit(corpus)
        bag_of_words = vec.transform(corpus)
        sum_words = bag_of_words.sum(axis=0) 
        words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
        words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
        return words_freq[:n]

    common_words = get_top_n_bigram(all_unprocessed_articles, 20)

    df3 = pd.DataFrame(common_words, columns = ['Review Text' , 'count'])
    common_bigram_words = df3.groupby('Review Text').sum()['count'].sort_values(ascending=False)

    fig = px.bar(common_bigram_words, x=common_bigram_words.index, y="count", title='Top 20 Bigram words in the News Articles before removing stop words')
    fig.update_traces(marker_color='darksalmon', marker_line_color='rgb(8,48,107)',
                    marker_line_width=0.9, opacity=0.6)

    fig.write_image("Top 20 Bigram words in the News Articles before removing stop words.png", scale=2.1934758155230596)

    ###############################################################################

    # Top 20 Bigram words in the News Articles after removing stop words
    common_words = get_top_n_bigram(all_processed_articles, 20)

    df3 = pd.DataFrame(common_words, columns = ['Review Text' , 'count'])
    common_bigram_words = df3.groupby('Review Text').sum()['count'].sort_values(ascending=False)

    fig = px.bar(common_bigram_words, x=common_bigram_words.index, y="count", title='Top 20 Bigram words in the News Articles after removing stop words')
    fig.update_traces(marker_color='darksalmon', marker_line_color='rgb(8,48,107)',
                    marker_line_width=0.9, opacity=0.6)

    fig.write_image("Top 20 Bigram words in the News Articles after removing stop words.png", scale=2.1934758155230596)

    ###############################################################################

    # Top 20 Trigram words in the News Articles before removing stop words
    def get_top_n_trigram(corpus, n=None):
        vec = CountVectorizer(ngram_range=(3, 3)).fit(corpus)
        bag_of_words = vec.transform(corpus)
        sum_words = bag_of_words.sum(axis=0) 
        words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
        words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
        return words_freq[:n]

    common_words = get_top_n_trigram(all_unprocessed_articles, 20)

    df5 = pd.DataFrame(common_words, columns = ['Review Text' , 'count'])
    top20trigrams = df5.groupby('Review Text').sum()['count'].sort_values(ascending=False)

    fig = px.bar(top20trigrams, x=top20trigrams.index, y="count", title='Top 20 Trigram words in the News Articles before removing stop words')
    fig.update_traces(marker_color='burlywood', marker_line_color='rgb(8,48,107)',
                    marker_line_width=0.9, opacity=0.6)

    fig.write_image("Top 20 Trigram words in the News Articles before removing stop words.png", scale=2.1934758155230596)

    ###############################################################################

    # Top 20 Trigram words in the News Articles after removing stop words
    common_words = get_top_n_trigram(all_processed_articles, 20)

    df5 = pd.DataFrame(common_words, columns = ['Review Text' , 'count'])
    top20trigrams = df5.groupby('Review Text').sum()['count'].sort_values(ascending=False)


    fig = px.bar(top20trigrams, x=top20trigrams.index, y="count", title='Top 20 Trigram words in the News Articles after removing stop words')
    fig.update_traces(marker_color='burlywood', marker_line_color='rgb(8,48,107)',
                    marker_line_width=0.9, opacity=0.6)

    fig.write_image("Top 20 Trigram words in the News Articles after removing stop words.png", scale=2.1934758155230596)

    ###############################################################################

    # The distribution of top part-of-speech tags of Pre-Processed News Articles
    blob = textblob.TextBlob(str(df['Preprocessed_Text_Content']))
    pos_df = pd.DataFrame(blob.tags, columns = ['word' , 'pos'])
    pos_df = pos_df.pos.value_counts()[:20]

    fig = px.bar(pos_df, x=pos_df.index, y="pos", title='The distribution of top part-of-speech tags of Pre-Processed News Articles')
    fig.update_traces(marker_color='lightcoral', marker_line_color='rgb(8,48,107)',)
    fig.update_xaxes(title='part-of-speech tags')
    fig.update_yaxes(title='count')
    fig.write_image("The distribution of top part-of-speech tags of Pre-Processed News Articles.png", scale=2.1934758155230596)

    ###############################################################################
