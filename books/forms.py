from django import forms
from django.contrib.auth.models import User
from books.models import *


class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text = "Please enter the book title.")
    year = forms.IntegerField(help_text = "Please enter publication year")
    publisher = forms.CharField(max_length=128,
                                help_text = "Please enter name of publisher")
    avg_rating = forms.DecimalField(widget=forms.HiddenInput(), initial=0,
                                    max_digits=3, decimal_places=2)
    author = forms.CharField(max_length=128,
                            help_text="Please enter name of author")
    cover = forms.ImageField(required=False,
                            help_text="Please submit a cover of the book")

    class Meta:
        model = Book
        fields =('title','author','year','publisher','avg_rating')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('avatar','no_reviews','books')

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1, max_value=5,
                                help_text="Please enter a rating between 1 and 5 stars")
    comment = forms.CharField(max_length=1000, required=False,
                             help_text="Enter your review here")
