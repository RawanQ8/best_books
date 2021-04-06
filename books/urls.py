from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('submit-book/',views.add_book, name='add_book'),
    path('search',views.book_list,name='book_list')
]
