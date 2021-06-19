from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields=("movie_name","movie_image")