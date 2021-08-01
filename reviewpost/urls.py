from django.urls import path
from .views import BooksIndex, BooksAbout, BooksMenu, BooksCreate, BooksOne, BooksTwo, BooksThree, BooksFour, BooksFive, BooksSix, BooksSeven, BooksEight, BooksNine, BooksTen

urlpatterns = [
    path('index/', BooksIndex.as_view(), name='index'),
    path('about/', BooksAbout.as_view(), name='about'),
    path('menu/', BooksMenu.as_view(), name='menu'),
    path('create/', BooksCreate.as_view(), name='create'),
    path('one/', BooksOne.as_view(), name='one'),
    path('two/', BooksTwo.as_view(), name='two'),
    path('three/', BooksThree.as_view(), name='three'),
    path('four/', BooksFour.as_view(), name='four'),
    path('five/', BooksFive.as_view(), name='five'),
    path('six/', BooksSix.as_view(), name='six'),
    path('seven/', BooksSeven.as_view(), name='seven'),
    path('eight/', BooksEight.as_view(), name='eight'),
    path('nine/', BooksNine.as_view(), name='nine'),
    path('ten/', BooksTen.as_view(), name='ten'),
]