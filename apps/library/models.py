from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import ExtraFieldsModelsMixin

class Library(ExtraFieldsModelsMixin, models.Model):
    name = models.CharField(_("Name"), max_length=100)
    location = models.CharField(_("Location"), max_length=100)

    def __str__(self):
        return self.name

class Book(ExtraFieldsModelsMixin, models.Model):
    title = models.CharField(_("Title"), max_length=100)
    author = models.CharField(_("Author"), max_length=100)
    publication_year = models.PositiveIntegerField(_("Publication Year"))
    genre = models.CharField(_("Genre"), max_length=50)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title