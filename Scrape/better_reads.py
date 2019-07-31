import bs4
import pandas as pd
import numpy as np
import requests as r
import re
import traceback
export_file_name = 'Best_Books_Ever.csv'

def initiate_1():
    # Target url to web scrape
    url = 'https://www.goodreads.com/list/show/1.Best_Books_Ever'

    # Get url and check status
    res = r.get(url)
    res.raise_for_status()

    # Initialize
    book_titles = []
    author = []
    ratings = []
    ids = []
    href = []

    # Instantiate and get html as text
    soup = bs4.BeautifulSoup(res.text)

    # Function Scraper
    def scrape(target_tag, inline_tag, inline_tag_name):
        # Parameters are strings
        attribute = soup.find_all(target_tag, {inline_tag: inline_tag_name})
        return [attr.text.strip('\n') for attr in attribute]

    for i in range(1, 567):

        print('Page ' + str(i))
        
        # Get current url
        res = r.get(url)
        # Check status - 200 is good
        res.raise_for_status()
        
        # Continuosly adding a new list into the variable
        
        print('Scraping ids')
        # Get id
        get_id = re.compile(r'^\d+')
        all_ids = [i.get('id') for i in soup.select('.u-anchorTarget')]
        for i in range(len(all_ids)):
            try:
                ids.append(get_id.search(all_ids[i]).group())
            except AttributeError:
                continue
        #ids += [i.get('id') for i in soup.select('.u-anchorTarget')[:100]]

        print('Scraping book titles')
        # Scrape book title
        book_titles += scrape('a', 'class', 'bookTitle')
        
        
        print('Scraping authors')
        # Scrape author
        author += scrape('span', 'itemprop', 'author')
        
        
        print('Scraping ratings')
        # Scrape rating
        ratings += scrape('span', 'class', 'minirating')

        print('Scraping href')
        # Scrape href
        href += [i.get('href') for i in soup.select('.bookTitle')]
        
        # Revise url and go to the next page
        next_page = soup.select('a[class="next_page"]')[0]
        url = 'https://www.goodreads.com'
        url = url  + next_page.get('href')

    # Change into series
    s1 = pd.Series(ids, name='id')
    s2 = pd.Series(book_titles, name='book_title')
    s3 = pd.Series(author, name='author')
    s4 = pd.Series(ratings, name='ratings')
    s5 = pd.Series(href, name='href')

    # Concat all into a dataframe
    df = pd.concat([s1,s2,s3,s4,s5], axis=1)

    # Export a csv file
    df.to_csv(export_file_name)

    print('Done')

initiate_1()

