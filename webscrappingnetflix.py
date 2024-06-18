import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.netflix.com/br/browse/genre/34399'

request = requests.get(url)

request.status_code # checking the requests status code 

page = request.content 

print(type(page)) 

# parsing the page with BeautifulSoup, to identify the tags and the HTML structures
page = BeautifulSoup(page, 'html.parser')

# looking for the unordered list with the specific class
ul = page.find('ul', attrs={'class': 'nm-content-horizontal-row-item-container'})

# initializing lists to hold movie names and their links
movies = []
hrefs = []

# looping through all list items to get movie names and links
for each_li in ul.findAll('li'):

    a_tag = each_li.find('a')  # finding the anchor tag in each list item
    hrefs.append(a_tag.get('href'))  # extracting and storing the link
    span = a_tag.find('span', attrs={'class': 'nm-collections-title-name'})
    
    if span:  # once the span with the movie title is found, i can extract the data
        movie_name = span.text  
        movies.append(movie_name) 

print(movies)
print(hrefs)

print(len(movies))

# creating a dictionary of movies and the links
movies_links = dict(zip(movies, hrefs))
movies_links

# creating a DataFrame from the lists of movies and links to visualize 
df = pd.DataFrame({'movies': movies, 'Link': hrefs})

print(df)
