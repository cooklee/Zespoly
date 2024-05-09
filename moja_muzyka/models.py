from django.db import models
from django.urls import reverse


# Create your models here.
class Band(models.Model):
    GENRES = (
        (-1, 'Not Define'),
        (0, 'rock'),
        (1, 'metal'),
        (2, 'pop'),
        (3, 'hio hop'),
        (4, 'electronic'),
        (5, 'reggae'),
        (6, 'other'),
    )
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=GENRES)

    def __str__(self):
        return f"{self.name} - {self.year}"

    def get_absolute_url(self):
        return reverse('band_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('band_delete', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)


class Article(models.Model):
    STATUS = (
        (1, 'w trakcie pisania'),
        (2, 'czeka na akceptacje'),
        (3, 'opublikowany'),
    )
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS)
    start_emission = models.DateField(null=True)
    end_emission = models.DateField(null=True)

    def get_start_emission_date(self):
        return self.start_emission.strftime("%Y-%m-%d")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('article_delete', kwargs = {'pk': self.pk})

class Album(models.Model):
    RAITING=(
        (1,'*'),
        (2,'**'),
        (3,'***'),
        (4,'****'),
        (5,'*****')
    )
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    raiting = models.IntegerField(choices=RAITING)