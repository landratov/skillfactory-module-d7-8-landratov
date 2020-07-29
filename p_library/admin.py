from django.contrib import admin
from .models import Book, Author, Publisher, Friend, UserProfile


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'age',
        'phone'
    )