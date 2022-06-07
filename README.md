# MINDS : Summer 2022 Programming Challenge

The goal of this programming exercise is to demonstrate your ability to design a solution to a
problem and implement this solution in Python using software engineering best practices.

The specific task will be to create a pipeline that collects and analyzes news articles from the web.
Given a short list of curated websites, your script should be able to collect the latest news articles
(via web scraping) and run them through some basic sentiment analysis.

## Installing Anaconda

If anaconda is not installed [Download link](https://www.anaconda.com/products/distribution), from this link follow the [Instructions to install anaconda](https://problemsolvingwithpython.com/01-Orientation/01.03-Installing-Anaconda-on-Windows/).

## Install Environment through .yml file (one line installation.)

Clone the repository to your local disk, In the repository there is a file named **minds_challenge_environment.yml**, to install all the dependencies in a single line, open **cmd** and enter the following command. 

```cmd
conda env create -f minds_challenge_environment.yml
```

## Note
**Important:** Sometimes in **cmd** it might say **'conda' is not recognized as internal or external command**, then follow this [link](https://www.google.com/search?q=conda+is+not+recognised+i+winodws&rlz=1C1FKPE_enIN986IN988&oq=conda+is+not+recognised+i+winodws&aqs=chrome..69i57.7799j0j1&sourceid=chrome&ie=UTF-8) to resolve this error. 

**Important:** If installation of environment doesn't work with .yml file, create an virtual environment and install all dependencies manually following the below commands. If installed successfully can skip the below manual environment creation and dependencies installation part.

## Manual - Creating and Using Virtual Environment

First step is to create anaconda virtual environment with python 3.9. 

```cmd
conda create -n minds_challenge python=3.9
```
To use the created conda virtual environment, it needs to be activated by following command. 

```cmd
conda activate minds_challenge 
```
## Installing required packages

To perform webscrapping in python, beautifulsoup, requests modules must be installed and to work with data from websites (storing, cleansing etc) pandas module is required.

```cmd
  pip install beautifulsoup4 requests pandas
```

To perform text preprocessing and sentiment analysis few packages are to be installed.

```cmd
  pip install contractions nltk inflect pyspellchecker textblob sklearn
```

To create visualizations and exporting plotly images and save them to disk, install plotly and kaleido packages.

```cmd
  pip install plotly kaleido 
```

## Brief explanation of scripts

### **main.py**

It contains all the abstract functions calls in pipeline that will run in order to webscrape the articles from the url, save it to a dataframe and return the dataframe, to preprocess the data and return a dataframe and display the preprocessing progress bar in the console using tqdm library, to perform the sentiment analysis on the dataframe given the column and save the results to the dataframe, to save the dataframe to CSV or JSON files, to make the visualizations and save them to disk and at the end display the time taken to run the script. Additionally it contains code to run the **main.py** script from CLI using argparse module, which also let's user to send or change default parameters before running the script.

### **web_scrapper.py**

It contains functions to scrape the data from the given url and return a dataframe, find pattern of dates in string such as '2022/6/06' return a list of dates and helper functions to save the dataframe to a csv or json file.

### **data_preprocessing.py**

It contains functions to remove round brackets, double quotes, punctuation and white space from the data, to convert the data to lower case, remove any contractions(e.g. don't -> do not), correct spellings of the data, to remove stopwords from the data, perform stemming or lemmatization on the data, to apply the preprocessing pipeline to the data and return the processed data and along with that a helper function to download the required nltk modules data for the preprocessing pipeline.

### **sentiment_analyzer.py**

It contains functions for nltk sentiment analysis using vader lexicon and to extract the sentiment score (float between -1 to 1) and the sentiment, for textblob sentiment analysis and to extract the sentiment score (float between -1 to 1) and the sentiment and to perform the sentiment analysis on the dataframe given the column and type of sentiment analyzer to use. Additionally it has a function to download the vader lexicon data from nltk.

### **visualizations.py**

It contains make_visualizations function which creates various plots on the processed data and save them to the disk.

## Default Usage/Examples

To run the script without changing any default parameters (whcih includes webscrapping, text preprocessing, sentiment analysis) run following command in cmd.

```cmd
python main.py
```

**Note :** If run for first time, it will take long time to run as it needs to download required sub modules for text preprocessing and sentiment analysis.

If script is successfully run it would look like this in cmd.

![CMD Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## User Entered Parameter Usage/Examples

User can change default parameters to get required results. To understand which parameter will result in what chnage, user can use **[-h]** command in cmd to find out more about parameters description.

```cmd
python main.py -h
```

This command gives all possible parameters which can be changed by the user, along with that it will give helpful description of what each parameter means. Below is screenshot of help command.

![Help Command Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


If user wants to save the web scrapped data, pre processed data, sentiment analysis results to csv, run the following command at cmd. Automatically a .csv file will be saved to script directory.

```cmd
python main.py --save_processed_data_to_CSV True
```

Similarly if user wants to save data in JSON format, use the following command.

```cmd
python main.py --save_processed_data_to_JSON True
```

If user wants to change sentiment analysis module, use follwoing command. (Default is NLTK_VADER, can change to TEXTBLOB)

```cmd
python main.py --kind TEXTBLOB
```

If user wants to include additional preprocessing such as Lemmatization or Stemming, use follwoing command. (Default is Stop Words, can change to LEMMATIZATION or STEMMING)

```cmd
python main.py --additional_preprocessing LEMMATIZATION
```

If user wants to save the plots to disk, use the following command.

```cmd
python main.py --make_visualizations True
```

If user wants to have multiple parameter's it is also possible. Below is the command to save the data to a .csv file, to include additional preprocessing Lemmatization, to create and save plots to disk, use the following command.

```cmd
python main.py --save_processed_data_to_CSV True --additional_preprocessing LEMMATIZATION --make_visualizations True
```

## Note

1. There is a optional --drop_empty_content_rows parameter, In egde cases where the article does not include any text content and only consists ofvideo, audio, etc., drop the row from the dataframe.

2. Also if user wish to include title and title paragraph of the news article, then they can use --include_title_and_title_paragraph parameter, to include title and title paragraph to the main article content and send it to pre-processing pipeline and later sentiment analysis and visualization.
## Visualizations Using Plotly

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Measured Script Run Time

Time Taken for script to web scrape the news articles from url and save them to dataframe and return the dataframe, then perform text pre processing and save the pre-processed text to dataframe, then perform sentiment analysis on the pre-processed text content and save results to dataframe and create and save visualizations for the analysis results is 48.99 seconds and without creating and saving visualizations it takes 35.36 seconds.

![Time taken to run the script](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![Time taken to run the script](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## Support

For support, email sree369nidhimindschallenge@gmail.com.

### **Author : Sreenidhi Iyengar Munimadugu**