from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book_author")
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL, related_name="book_publisher")
    cover = models.ImageField(upload_to='books', blank=True)

    def __str__(self):
        return self.title


class Friend(models.Model):
    name = models.TextField(verbose_name=_("Имя"))
    books = models.ManyToManyField(Book, related_name="friend_book", blank=True, verbose_name=_("Книги"))

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    age = models.IntegerField(blank=True)
    phone = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return self.user.username
