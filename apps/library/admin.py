from django.contrib import admin

from apps.library.models import Library, Book

# Register your models here.

admin.site.register(Library)
admin.site.register(Book)