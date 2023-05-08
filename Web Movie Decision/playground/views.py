from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import Info
import get_data as g
import socket
socket.setdefaulttimeout(150 * 6000)

def crit(response):
    if response.method == "POST":
        form = Info(response.POST)

        if form.is_valid():
            movie_series = form.cleaned_data["movie_series"] 
            genre = form.cleaned_data["genre"]
            year = form.cleaned_data["year"]
            rating = form.cleaned_data["rating"]
            
            data = g.Generator(movie_series, genre, year, rating).gen_out()

            title = data[0]
            year = data[1]
            genre = data[2]
            rating = data[3]
            plot = data[4]
            cover = data[5]
            r = data[6]
            return render(response, "WMD.html", {"form":form,
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
