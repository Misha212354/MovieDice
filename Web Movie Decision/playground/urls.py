from django.urls import path
from . import views

urlpatterns = [
    path("crit/", views.crit)
]