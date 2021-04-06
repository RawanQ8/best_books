from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.


class Book (models.Model):
    title = models.CharField(max_length=128, unique=True)
    year = models.IntegerField(default=2021)
    publisher = models.CharField(max_length=128)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    #url = models.URLField(unique=True)
    cover = models.ImageField(upload_to='covers', blank=True)
    authors = models.CharField(max_length=256)
    user = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Book,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='avatars', blank=True)
    no_reviews = models.IntegerField(default=0)
    books = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.User.username

class Review(models.Model):
    rating = models.IntegerField(default=0)
    comment = models.CharField(max_length=1000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class Author(models.Model):
    name = models.CharField(max_length=128, unique =True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
