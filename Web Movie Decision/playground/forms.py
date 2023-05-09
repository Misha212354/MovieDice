from django import forms
import datetime

CHOICES = [('1', 'Movie'), ('2', 'Series')]

GENRE_CHOICES = [
    ('action', 'Action'),
    ('adventure', 'Adventure'),
    ('animation', 'Animation'),
    ('biography', 'Biography'),
    ('comedy', 'Comedy'),
    ('crime', 'Crime'),
    ('documentary', 'Documentary'),
    ('drama', 'Drama'),
    ('family', 'Family'),
    ('fantasy', 'Fantasy'),
    ('film-noir', 'Film Noir'),
    ('history', 'History'),
    ('horror', 'Horror'),
    ('music', 'Music'),
    ('musical', 'Musical'),
    ('mystery', 'Mystery'),
    ('romance', 'Romance'),
    ('sci-fi', 'Sci-Fi'),
    ('short-film', 'Short Film'),
    ('sport', 'Sport'),
    ('superhero', 'Superhero'),
    ('thriller', 'Thriller'),
    ('war', 'War'),
    ('western', 'Western'),
]


class Info(forms.Form):
    
    movie_series = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    genre = forms.ChoiceField(choices=GENRE_CHOICES,  widget=forms.Select(attrs={'class': 'genre-select'}))
    
    year = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'year-inp',
            'placeholder': 'Year',
            'min': '1900',
            'max': '2022'
        }),
        min_value=1900,
        max_value=datetime.datetime.now().year
    )

    rating = forms.FloatField(
        label="Rating",
        widget=forms.NumberInput(attrs={
            "class": "rating-inp",
            "placeholder": "Rating",
            "step": "0.1",
            "min": "0.0",
            "max": "10.0"
        })
    )
    
