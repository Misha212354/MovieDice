from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import Info
from get_data import Generator as Generator
import socket
from django.shortcuts import redirect


socket.setdefaulttimeout(150 * 6000)
title = 0
year = 0
genre = 0
rating = 0
plot = 0
cover = 0
r = 0

#create generate data function use it for movie

def find_movies(response):
    if response.method == "POST":
        form = Info(response.POST)

        if form.is_valid():
            movie_series = form.cleaned_data["movie_series"] 
            genre = form.cleaned_data["genre"]
            year = form.cleaned_data["year"]
            rating = form.cleaned_data["rating"]

            generator = Generator(genre, year, rating)

            if (movie_series == "1"): 
                generator.get_movies()

            if (movie_series == "2"):
                generator.get_tv_shows()

            generator.year_rating_clean()

            chosen = generator.make_choice()

            title = chosen[0]
            year = chosen[1]
            genre = chosen[2]
            rating = chosen[3]
            plot = chosen[4]
            cover = chosen[5]
            r = chosen[6]
            return render(response, "movie_page.html", {"form":form,
                                                "title":title, 
                                                "year":year, 
                                                "genre":genre, 
                                                "rating":rating, 
                                                "plot":plot,
                                                "cover":cover,
                                                "r":r})
            
    else:    
        form = Info()
    return render(response, "WMD.html", {"form":form})

def welcome_view(request):
    return render(request, "welcome.html")