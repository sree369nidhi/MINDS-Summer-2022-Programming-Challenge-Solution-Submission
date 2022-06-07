##main script
from web_scrapper import web_scrapper, save_to_json, save_to_csv
from data_preprocessing import preprocessing_pipeline, nltk_preprocessing_required_downloads
from tqdm.auto import tqdm
from sentiment_analyzer import sentiment_analyzer, sentiment_analysis_required_downloads
import timeit
import argparse
import os
import pandas as pd
from visualizations import make_visualizations


if __name__ == '__main__':

    ##############################################################################

    # code to craete and parse the arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('--drop_empty_content_rows', type=bool, required=False, default=False, help='If "True", In egde cases where the article does not include any text content other than video, audio, etc., drop the row from the dataframe.')
    parser.add_argument('--include_title_and_title_paragraph', type=bool, required=False, default=False, help='If "True" Title and Title Paragraph will be added to main article content for preprocessing and sentiment analysis.')
    parser.add_argument('--kind', type=str, required=False, default='NLTK_VADER', help='Kind of pre-trained sentiment analysis model to be used to perform the analysis. NLTK_VADER or TEXTBLOB.')
    parser.add_argument('--additional_preprocessing', type=str, required=False, default='Stop Words', help='Additional Preprocessing fucntions to be used. LEMMATIZATION or STEMMING.')
    parser.add_argument('--save_processed_data_to_CSV', type=bool, required=False, default=False, help='If "True", Save processed data as CSV at Script Directory. Default is False.')
    parser.add_argument('--save_processed_data_to_JSON', type=bool, required=False, default=False, help='If "True", Save processed data as JSON at Script Directory. Default is False.')
    parser.add_argument('--make_visualizations', type=bool, required=False, default=False, help='If "True", visualizations for the sentiment analysis outputs for the preprocessed data will be made using plotly and saved to disk at Script Directory.')

    args = parser.parse_args()

    ###############################################################################

    #code to start the timer
    starttime = timeit.default_timer()

    ###############################################################################

    #code to scrape the data from the web, save it to a dataframe and return the dataframe
    given_url = 'https://www.aljazeera.com/where/mozambique/'
    base_url = 'https://www.aljazeera.com'

    news_df = web_scrapper(given_url, base_url, drop_empty_content_rows=args.drop_empty_content_rows, include_title_and_title_paragraph=args.include_title_and_title_paragraph)

    ###############################################################################
    
    #code to preprocess the data and return a dataframe and display the preprocessing progress bar in the console using tqdm library
    nltk_preprocessing_required_downloads()

    tqdm.pandas(desc='Preprocessing Text Content...')
    news_df['Preprocessed_Text_Content'] = news_df['Text_Content'].progress_apply(preprocessing_pipeline, additional_preprocessing=args.additional_preprocessing)

    ###############################################################################

    #code to perform the sentiment analysis on the dataframe given the column and save the results to the dataframe
    sentiment_analysis_required_downloads()

    sentiment_analyzer(news_df, 'Preprocessed_Text_Content', kind=str(args.kind))

    ###############################################################################

    #code to save the dataframe to CSV or JSON files
    if args.save_processed_data_to_CSV:
        save_to_csv(news_df)
    if args.save_processed_data_to_JSON:
        save_to_json(news_df)

    ###############################################################################

    #code to make the visualizations and save them to disk
    if args.make_visualizations:
        make_visualizations(news_df)
    
    ##############################################################################

    #code to stop the timer and display the time taken to run the script
    print("The time taken for the script to run is : ", timeit.default_timer() - starttime)

    ###############################################################################