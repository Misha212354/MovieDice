from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome_view),
    path("find_movies/", views.find_movies)
]