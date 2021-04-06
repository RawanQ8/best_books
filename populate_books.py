import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'best_books.settings')
import django
django.setup()
from books.models import Book, Review, Author

def populate():

    uploaded_books = [
        {'title':'Harry Potter', 'year':1998, 'publisher':'penguin',
        'cover':'static/images/HarryPotter.jpg','author':'TERF'},
        {'title':'Hunger Games', 'year':2000, 'publisher':'penguin',
        'cover':'static/images/Hunger-Games.jpg','author':'Katniss'},
        {'title':'ASTF', 'year':2015, 'publisher':'penguin',
        'cover':'static/images/astf.jpg','author':'Cammie'},
    ]

    HP_reviews = [{'rating':5}, {'rating':3, 'comment':'liked book, hated author'},
                {'rating':4},{'rating':4}, {'rating':1}, {'rating':5}]

    HG_reviews[{'rating':5, 'comment':'best book ever'}, {'rating':2},
                {'rating':4, 'comment':'meh'}]

    ASTF_reviews[{'rating':5}]
