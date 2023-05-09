import imdb
import pandas as pd
from datetime import date
import random
import socket
import numpy as np 

pd.set_option('mode.chained_assignment', None)
socket.setdefaulttimeout(300 * 6000)


# creating an instance of the IMDB()
moviesDB = imdb.IMDb()

# Using the Search movie method
class Generator:
    def __init__(self, genre, year, rating):    #, results_num
        self.genre = str(genre.lower())
        self.year = int(year)
        self.rating = float(rating)
        self.list = []
        
    def get_movies(self):
        #get top 50 movies by genre
        sub_DB = moviesDB.get_top50_movies_by_genres(self.genre)

        #get additional movies (web scraping)
        df = pd.read_csv('https://www.imdb.com/list/ls024863935/export', header=0, usecols=["Title", "Title Type", "IMDb Rating", "Year",  "Genres", "Release Date"])
        df.rename(columns={"Title": "title", "IMDb Rating": "rating", "Year": "year", "Genres":"genre"}, inplace=True)

        for i in range(len(df["genre"])):
            df["genre"][i] = (df["genre"][i].replace(" ", "")).split(",")

        for i in range(len(df["Title Type"])):
            if df["Title Type"][i] == 'movie':
                sub_DB.append(df.loc[i])
        
        self.list = sub_DB

    def get_tv_shows(self):
        #get top 50 tv shows by genre
        sub_DB = moviesDB.get_top50_movies_by_genres(self.genre)

        df = pd.read_csv('https://www.imdb.com/list/ls024863935/export', header=0, usecols=["Title", "Title Type", "IMDb Rating", "Year",  "Genres", "Release Date"])
        df.rename(columns={"Title": "title", "IMDb Rating": "rating", "Year": "year", "Genres":"genre"}, inplace=True)

        for i in range(len(df["genre"])):
            df["genre"][i] = (df["genre"][i].replace(" ", "")).split(",")

        for i in range(len(df["Title Type"])):
            if df["Title Type"][i] == 'movie':
                sub_DB.append(df.loc[i])
        
        self.list = sub_DB

    def year_rating_clean(self):
        new_list = []

        for n in self.list:
            if n.get("year") != None and n.get("rating") != None and len(n["genre"]) != 0:
                if n["year"] == self.year and n["year"] <= date.today().year and n["rating"] >= self.rating and self.genre in np.char.lower(n["genre"]):
                    new_list.append(n)

        if(len(new_list) == 0):
            for n in self.list:
                if n.get("year") != None and n.get("rating") != None and len(n["genre"]) != 0:
                    if n["year"] >= self.year and n["year"] <= date.today().year and n["rating"] >= self.rating and self.genre in np.char.lower(n["genre"]):
                        new_list.append(n)

        self.list = new_list

    def make_choice(self):
        if len(self.list) != 0:
            rand = random.choice(self.list)
            
            chosen_movie = moviesDB.search_movie_advanced(str(rand['title']))[0]
            
            url = chosen_movie["cover url"]
            
            #Improve image quality, cuts the url to get to a good quality
            if "@" in url:
                url = url[:url.rindex('@')+1]

            if type(chosen_movie['plot']) == str:
                return chosen_movie["title"], chosen_movie["year"], ', '.join([str(element) for element in chosen_movie['genre']]), chosen_movie["rating"], chosen_movie["plot"], url, "We recommend"
            else:
                return chosen_movie["title"], chosen_movie["year"], ', '.join([str(element) for element in chosen_movie['genre']]), chosen_movie["rating"], "No plot available", url, "We recommend"
        else:
            return "No title", "No year", "No genre", "No rating", "No plot", "No url", "We recommend"
        


# movie_series = "1"
# genre = "action"
# year = "2015"
# rating = "7"

# generator = Generator(genre, year, rating)

# if (movie_series == "1"): 
#     generator.get_movies()

# if (movie_series == "2"):
#     generator.get_tv_shows()

# generator.year_rating_clean()

# chosen = generator.make_choice()

# title = chosen[0]
# year = chosen[1]
# genre = chosen[2]
# rating = chosen[3]
# plot = chosen[4]
# cover = chosen[5]
# r = chosen[6]