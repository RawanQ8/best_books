from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from books.models import Book, Review
from books.forms import BookForm, UserForm, UserProfileForm, ReviewForm

# Create your views here.

def home(request):
    top_books = Book.objects.order_by('-avg_rating')[:5]
    context_dict ={'books':top_books}
    return render(request, 'books/home.html', context_dict)

def about (request):
    context_dict ={}
    return render(request,'books/about.html', context_dict)

@login_required
def add_book(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.isValid():
            form.save(commit=True)
            return redirect(reverse('books:home'))
        else:
            print(form.errors)

    return render(request, 'books/add_Book.html', {'form':form})
