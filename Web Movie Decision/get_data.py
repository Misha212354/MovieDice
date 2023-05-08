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
    def __init__(self, m_or_s, genre, year, rating):    #, results_num
        self.m_or_s = m_or_s.lower()
        self.genre = str(genre.lower())
        self.year = int(year)
        self.rating = float(rating)
        
    
    def gen_out(self):
        #Movie or TV series###################################################################
        if(self.m_or_s == "1"):
            sub_DB = moviesDB.get_top50_movies_by_genres(self.genre)


            df = pd.read_csv('https://www.imdb.com/list/ls024863935/export', header=0, usecols=["Title", "Title Type", "IMDb Rating", "Year",  "Genres", "Release Date"])
            df.rename(columns={"Title": "title", "IMDb Rating": "rating", "Year": "year", "Genres":"genre"}, inplace=True)

            for i in range(len(df["genre"])):
                df["genre"][i] = (df["genre"][i].replace(" ", "")).split(",")

            for i in range(len(df["Title Type"])):
                if df["Title Type"][i] == 'movie':
                    sub_DB.append(df.loc[i])
            
        
        if(self.m_or_s == "2"):
            sub_DB = moviesDB.get_top50_tv_by_genres(self.genre)

            
            df = pd.read_csv("https://www.imdb.com/list/ls000033724/export", header=0, usecols=["Title", "Title Type", "IMDb Rating", "Year",  "Genres", "Release Date"])
            df.rename(columns={"Title": "title", "IMDb Rating": "rating", "Year": "year", "Genres":"genre"}, inplace=True)

            for i in range(len(df["genre"])):
                df["genre"][i] = (df["genre"][i].replace(" ", "")).split(",")

            for i in range(len(df["Title Type"])):
                sub_DB.append(df.loc[i])
        ######################################################################################

        #Parse through years and rating#######################################################
        g =[]
        for n in sub_DB:
            if n.get("year") != None and n.get("rating") != None and len(n["genre"]) != 0:
                if n["year"] >= self.year and n["year"] <= date.today().year and n["rating"] >= self.rating and self.genre in np.char.lower(n["genre"]):
                    g.append(n)
        sub_DB = g
        ######################################################################################
        if len(sub_DB) != 0:
            rand = random.choice(sub_DB)
            
            chosen_movie = moviesDB.search_movie_advanced(str(rand['title']))[0]
            url = chosen_movie["cover url"]
            url = url[:url.rindex('@')+1]
            if type(rand['plot']) == str:
                return rand["title"], rand["year"], ', '.join([str(element) for element in rand['genre']]), rand["rating"], rand["plot"], url, "We recommend"
            else:
                return rand["title"], rand["year"], ', '.join([str(element) for element in rand['genre']]), rand["rating"], "No plot available", url, "We recommend"
        else:
            print("There is no such movies \n")
        

