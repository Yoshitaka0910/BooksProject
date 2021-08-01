from django import forms
from django.forms import fields
from .models import BooksModel

class ArticleForm(forms.ModelForm):

    class Meta:
        model = BooksModel
        fields = ('category', 'title', 'author', 'content', 'images')