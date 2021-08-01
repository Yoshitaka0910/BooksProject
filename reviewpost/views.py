from .models import BooksModel
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .forms import ArticleForm

class BooksIndex(TemplateView):
    template_name = 'index.html'

class BooksAbout(TemplateView):
    template_name = 'about.html'

class BooksMenu(TemplateView):
    template_name = 'menu.html'

class BooksCreate(CreateView):
    form_class = ArticleForm
    template_name = 'create.html'
    success_url = reverse_lazy('menu')

class BooksOne(ListView):
    template_name = 'one.html'
    model = BooksModel

class BooksTwo(ListView):
    template_name = 'two.html'
    model = BooksModel

class BooksThree(ListView):
    template_name = 'three.html'
    model = BooksModel

class BooksFour(ListView):
    template_name = 'four.html'
    model = BooksModel

class BooksFive(ListView):
    template_name = 'five.html'
    model = BooksModel

class BooksSix(ListView):
    template_name = 'six.html'
    model = BooksModel

class BooksSeven(ListView):
    template_name = 'seven.html'
    model = BooksModel

class BooksEight(ListView):
    template_name = 'eight.html'
    model = BooksModel

class BooksNine(ListView):
    template_name = 'nine.html'
    model = BooksModel

class BooksTen(ListView):
    template_name = 'ten.html'
    model = BooksModel