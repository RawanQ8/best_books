from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from books.models import Book, Review, UserProfile
from books.forms import BookForm, UserForm, UserProfileForm, ReviewForm

# Create your views here.

def home(request):
    top_books = Book.objects.order_by('-avg_rating')[:5]
    context_dict ={'books':top_books}
    return render(request, 'books/home.html', context_dict)

def about (request):
    context_dict ={}
    return render(request,'books/about.html', context_dict)

def show_book (request, book_name_slug):
    context_dict = {}
    reviews = Review.objects.filter(book=book_name_slug)
    try:
        book = Book.objects.get(slug=book_name_slug)
        context_dict['book'] = book
        context_dict['reviews'] = reviews

    except Book.DoesNotExist:
        context_dict['book'] = None
        context_dict['reviews'] = None
    return render(request, 'books/book.html', context=context_dict)

def book_list(request):
    all_books = Book.objects.all()
    context_dict={'books':all_books}

    return render(request,'books/allBooks.html', context=context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                    'book/register.html',
                    context={'user_form':user_form,
                              'profile_form':profile_form,
                              'registered':registered})

def user_login(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('books:home'))
            else:
                return HttpResponse("Your Best Books account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'books/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('books:home'))

@login_required
def view_account(request):
    context_dict = {'no_reviews':UserProfile.no_reviews,
                    'name':UserProfile.user.username}


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

@login_required
def add_review(request, book):

    form = ReviewForm()
    reviewBook = Book.objects.get(title=book)
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.isValid():
            data = form.save(commit=True)
            data.comment = request.POST['comment']
            data.rating = request.POST['rating']
            data.user = request.user
            data.book = book
            data.save()
            return redirect(reverse('books:allBooks:<data.book.slug>'))
        else:
            print(form.errors)

    return render(request, 'books/add_review.html', {'form':form})

# def getAvgRating(book):
#     totalRating = 0
#     reviews[] = Review.objects.all()
#     for r in reviews:
#         totalRating += r.rating
