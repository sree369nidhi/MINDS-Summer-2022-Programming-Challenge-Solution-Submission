# MINDS: Summer 2022 Programming Challenge

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

**Important:** If the installation of the environment doesn't work with the .yml file, create a virtual environment and install all dependencies manually following the below commands. If installed successfully can skip the below manual environment creation and dependencies installation part.

## Manual - Creating and Using Virtual Environment

The first step is to create an anaconda virtual environment with python 3.9. 

```cmd
conda create -n minds_challenge python=3.9
```
To use the created conda virtual environment, it needs to be activated by the following command. 

```cmd
conda activate minds_challenge 
```
## Installing required packages

To perform web scraping in python, beautifulsoup, requests modules must be installed, and to work with data from websites (storing, cleansing, etc) pandas module is required.

```cmd
  pip install beautifulsoup4 requests pandas
```

To perform text preprocessing and sentiment analysis few packages are to be installed.

```cmd
  pip install contractions nltk inflect pyspellchecker textblob sklearn
```

To create visualizations and export plotly images and save them to disk, install plotly and kaleido packages.

```cmd
  pip install plotly kaleido 
```

## Brief explanation of scripts

### **main.py**

It contains all the abstract functions calls in the pipeline that will run in order to web scrape the articles from the URL, save them to a data frame and return the data frame, preprocess the data and return a data frame and display the preprocessing progress bar in the console using tqdm library, to perform the sentiment analysis on the data frame given the column and save the results to the data frame, to save the data frame to CSV or JSON files, to make the visualizations and save them to disk and at the end display the time taken to run the script. Additionally, it contains code to run the **main.py** script from CLI(CMD) using the argparse module, which also lets users send or change default parameters before running the script.

### **web_scrapper.py**

It contains functions to scrape the data from the given URL and return a data frame, find a pattern of dates in strings such as '2022/6/06' return a list of dates, and helper functions to save the data frame to a CSV or JSON file.

### **data_preprocessing.py**

It contains functions to remove round brackets, double quotes, punctuation, and white space from the data, convert the data to lower case, remove any contractions(e.g. don't -> do not), correct spellings of the data, remove stopwords from the data, perform stemming or lemmatization on the data, to apply the preprocessing pipeline to the data and return the processed data and along with that a helper function to download the required nltk modules data for the preprocessing pipeline.

### **sentiment_analyzer.py**

It contains functions for nltk sentiment analysis using Vader lexicon and to extract the sentiment score (float between -1 to 1) and the sentiment, for textblob sentiment analysis and to extract the sentiment score (float between -1 to 1) and the sentiment and to perform the sentiment analysis on the data frame given the column and type of sentiment analyzer to use. Additionally, it has a function to download the Vader lexicon data from nltk.

### **visualizations.py**

It contains the make_visualizations function which creates various plots on the processed data and saves them to the disk.

## Default Usage/Examples

To run the script without changing any default parameters (which includes web scrapping, text preprocessing, and sentiment analysis) run the following command in cmd.

```cmd
python main.py
```

**Note:** If run for the first time, it will take a long time to run as it needs to download the required sub modules for text preprocessing and sentiment analysis.

If the script is successfully run it would look like this in cmd.

![CMD Screenshot](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Helper%20Screenshots/default%20cmd%20screenshot.jpg)

## User Entered Parameter Usage/Examples

Users can change default parameters to get the required results. To understand which parameter will result in what changes, the user can use the **[-h]** command in cmd to find out more about the description of the parameters.

```cmd
python main.py -h
```

This command gives all possible parameters which can be changed by the user, and along with that, it will give a helpful description of what each parameter means. Below is a screenshot of the help command.

![Help Command Screenshot](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Helper%20Screenshots/help%20command%20for%20script%20screenshot.jpg)


If the user wants to save the web scrapped data, pre-processed data, and sentiment analysis results to CSV, run the following command at cmd. Automatically a .csv file will be saved to the script directory.

```cmd
python main.py --save_processed_data_to_CSV True
```

Similarly, if the user wants to save data in JSON format, use the following command.

```cmd
python main.py --save_processed_data_to_JSON True
```

If the user wants to change the sentiment analysis module, use the following command. (Default is NLTK_VADER, can change to TEXTBLOB)

```cmd
python main.py --kind TEXTBLOB
```

If the user wants to include additional preprocessing such as Lemmatization or Stemming, use the following command. (Default is Stop Words, can change to LEMMATIZATION or STEMMING)

```cmd
python main.py --additional_preprocessing LEMMATIZATION
```

If the user wants to save the plots to disk, use the following command.

```cmd
python main.py --make_visualizations True
```

If the user wants to have multiple parameters it is also possible. Below is the command to save the data to a .csv file, to include additional preprocessing Lemmatization, to create and save plots to disk, use the following command.

```cmd
python main.py --save_processed_data_to_CSV True --additional_preprocessing LEMMATIZATION --make_visualizations True
```

## Note

1. There is an optional --drop_empty_content_rows parameter, In edge cases where the article does not include any text content and only consists of video, audio, etc., drop the row from the data frame.

2. Also if users wish to include the title and title paragraph of the news article, then they can use --include_title_and_title_paragraph parameter, to include the title and title paragraph to the main article content and send it to pre-processing pipeline and later sentiment analysis and visualization.

## Visualizations Using Plotly

![Visualization Screenshot](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Plots/Histogram%20of%20Sentiment%20Polarity%20(categories)%20Distribution.png)

![Visualization Screenshot](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Plots/Length%20of%20the%20text%20(count%20of%20words%20in%20Thousands).png)


![Visualization Screenshot](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Plots/Sentiment%20Polarity%20Box%20plot.png)


![Visualization Screenshot](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Plots/Top%2020%20words%20in%20the%20News%20Articles%20before%20removing%20stop%20words.png)


![Visualization Screenshot](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Plots/Top%2020%20words%20in%20the%20News%20Articles%20after%20removing%20stop%20words.png)


![Visualization Screenshot](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Plots/Top%2020%20Bigram%20words%20in%20the%20News%20Articles%20before%20removing%20stop%20words.png)

![Visualization Screenshot](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Plots/Top%2020%20Bigram%20words%20in%20the%20News%20Articles%20after%20removing%20stop%20words.png)


![Visualization Screenshot](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Plots/Top%2020%20Trigram%20words%20in%20the%20News%20Articles%20before%20removing%20stop%20words.png)

![Visualization Screenshot](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Plots/Top%2020%20Trigram%20words%20in%20the%20News%20Articles%20after%20removing%20stop%20words.png)


![Visualization Screenshot](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Plots/The%20distribution%20of%20top%20part-of-speech%20tags%20of%20Pre-Processed%20News%20Articles.png)


## Measured Script Run Time

Time Taken for the script to web scrape the news articles from URL and save them to data frame and return the data frame, then perform text pre-processing and save the pre-processed text to the data frame, then perform sentiment analysis on the pre-processed text content and save results to data frame and create and save visualizations for the analysis results is 48.99 seconds and without creating and saving visualizations it takes 35.36 seconds.

![Time taken to run the script](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Helper%20Screenshots/measured%20script%20run%20time%20with%20creating%20and%20saving%20visualizations%20screenshot.jpg)

![Time taken to run the script](https://github.com/sree369nidhi/MINDS-Summer-2022-Programming-Challenge-Solution-Submission/blob/main/Helper%20Screenshots/measured%20script%20run%20time%20wihtout%20creating%20and%20saving%20visualizations%20screenshot.jpg)

## Support

For support, email sree369nidhimindschallenge@gmail.com.

### **Author : Sreenidhi Iyengar Munimadugu**