import bs4
import pandas as pd
import requests as r
import re
import traceback
import numpy as np

header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

# Save df - Need the href
df = pd.read_csv('Best_Books_Ever.csv')

# Target website
url = 'https://www.goodreads.com'

# Change accordingly for each scrape iteration
number = '2' 
start = 3000
end = 5000

# Initialize empty list
original_title = []
isbn = []
edition_language = []
series = []
characters = []
setting = []
literary_awards = []

genres_list = []

list_ = [original_title, isbn, edition_language, series, characters, setting, literary_awards]

# The features we want scraped
names = ['Original Title', 'ISBN', 'Edition Language', 'Series', 'Characters', 'setting', 'Literary Awards']

# More Details - Scrape
def more_details_scrape():

    # The container we want to scrape
    details_1 = soup.find_all('div', {'class': 'infoBoxRowTitle'})
    details_2 = soup.find_all('div', {'class': 'infoBoxRowItem'})
    details_1_list = [details_1[i].text for i in range(len(details_1))]
    details_2_list = [details_2[i].text for i in range(len(details_2))]


    # Loop through the names and scrape the info or append null
    for j in range(len(names)):
        try:
            if names[j] in details_1_list:

                list_[j].append(details_2[details_1_list.index(names[j])].text.strip('\n')
                                .replace('\n', ' ').replace('  ', ' ').strip(' '))
            else:
                list_[j].append(np.nan)

        except IndexError:
            list_[j].append(np.nan)

    print('--- More Details has been Scraped ---')

# Genre Scrape
def genre_scrape():

    genres = []

    # Find the container holding the genre
    genre = soup.find_all('a', {'class': 'actionLinkLite bookPageGenreLink'})
    print('--- Genres has been Scraped ---', '\n')

    # Loop and append the genres
    for l in range(len(genre)):
        genres.append(genre[l].text)

    genres_list.append(genres)

    # Change into series and combine details and genre
    combine_list = list_ + [genres]
    combine_list_names = ['original_title', 'isbn', 'edition_language', 'series', 
                          'characters', 'setting', 'literary_awards', 'genres']

    # Make the combine_list into 
    series_list = []

    # Append the series into the series list
    for k in range(len(combine_list)):
        series_list.append(pd.Series(combine_list[k], name=combine_list_names[k]))


# Initiate the scrape
for i in range(start, end):

    # Request and check if site in online
    res = r.get(url + df['href'][i], headers=header)
    res.raise_for_status()

    # Instantiate the bs4
    soup = bs4.BeautifulSoup(res.text)
    
    print(f"Now Scraping: {i} {df['book_title'][i]}")
          
    more_details_scrape()

    genre_scrape()

# Concat all into a dataframe
series = [pd.Series(list_[i], name=names[i]) for i in range(len(names))]
genres_series = pd.Series(genres_list, name='Genre')
series.append(genres_series)

df_more = pd.concat(series, axis=1)

# Export to csv
df_more.to_csv('more_detail_genre' + number + '.csv')

print('Done')