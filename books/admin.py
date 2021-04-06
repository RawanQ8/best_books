from django.contrib import admin
from books.models import *
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'year', 'avg_rating')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'comment')
# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile)
