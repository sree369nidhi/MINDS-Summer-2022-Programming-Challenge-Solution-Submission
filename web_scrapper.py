##webscrapping the data
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import os
import re

###############################################################################

# find pattern of dates in string such as '2022/5/23' return a list of dates 
def pattern_match(string):
    date_extract_pattern = "[0-9]{4}\\/[0-9]{1,2}\\/[0-9]{1,2}"
    return re.findall(date_extract_pattern, string)[0]

###############################################################################

# code to scrape the data from the given url and return a dataframe
def web_scrapper(given_url, base_url, drop_empty_content_rows=False, include_title_and_title_paragraph=False):
    given_url = given_url
    base_url = base_url

    response = requests.get(given_url)
    soup = bs(response.content, 'html.parser')
    a_tags = soup.findAll("a",attrs={"class","u-clickable-card__link"})

    urls = []

    for a_tag in a_tags:
        urls.append(a_tag.attrs['href'])

    urls_df = pd.DataFrame(urls, columns=['url'])

    urls_df['Date'] = urls_df['url'].apply(pattern_match)

    urls_df['Date'] = pd.to_datetime(urls_df['Date'])
    urls_df.set_index(urls_df['Date'], inplace=True)
    urls_df.drop(['Date'], axis=1, inplace=True)

    urls_df.sort_index(ascending=False, inplace=True)

    title_list = list()
    title_paragraph_list = list()
    main_content_list = list()

    for i in urls_df.index:

        response = requests.get(base_url + urls_df.loc[i, 'url'])
        soup = bs(response.content, 'html.parser')

        try:
            title = soup.find("h1")
            title_list.append(title.text)
        except:
            title_list.append('Title not found')

        try:
            para = soup.find("p")
            title_paragraph_list.append(para.text)
        except: 
            title_paragraph_list.append('No Paragraph')

        try:
            main_content = soup.find_all("div", attrs= {"class":"wysiwyg wysiwyg--all-content css-1ck9wyi"})
            main_content_list.append(main_content[0].text.replace('\n', ' '))
        except:
            main_content_list.append('   ')

    urls_df['Title'] = title_list
    urls_df['Title_Paragraph'] = title_paragraph_list
    urls_df['Main_Content'] = main_content_list

    if drop_empty_content_rows:
        urls_df = urls_df[urls_df['Main_Content'] != '   ']
    
    if include_title_and_title_paragraph:
        urls_df['Text_Content'] = urls_df['Title'] + ' ' + urls_df['Title_Paragraph'] + ' ' + urls_df['Main_Content']
    else:
        urls_df['Text_Content'] = urls_df['Main_Content']

    return urls_df.head(10)

###############################################################################

# code to save the dataframe to a json file
def save_to_json(urls_df):
    cwd = os.getcwd()
    urls_df.to_json(os.path.join(cwd, "Web_Scrapped_Original_and_Text_PreProcessed_Data_with_Sentiment_Results.json"))

###############################################################################

# code to save the dataframe to a csv file
def save_to_csv(urls_df):
    cwd = os.getcwd()
    urls_df.to_csv(os.path.join(cwd, "Web_Scrapped_Original_and_Text_PreProcessed_Data_with_Sentiment_Results.csv"))

###############################################################################