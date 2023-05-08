from django import forms

class Info(forms.Form):
    CHOICES = [('1', 'Movie'), ('2', 'Series')]
    movie_series = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    genre = forms.CharField(label="Genre")
    year = forms.CharField(label="Year")
    rating = forms.CharField(label="Rating")
    
