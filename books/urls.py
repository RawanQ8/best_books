from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('all-books/', views.book_list, name='all-books'),
    path('book/<slug:book_name_slug>/',
        views.show_book, name='show_book'),
    path('submit_book/', views.add_book, name='add_book'),
    path('book/<slug:book_name_slug>/add_review',
        views.add_review, name='add_review'),
    path('sign-up/', views.register, name='sign-up'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

]
