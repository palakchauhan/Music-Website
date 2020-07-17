from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
#a blueprint for database, a template of how youll store data


class Album(models.Model):#table name
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    logo = models.FileField(max_length=1000)

    def get_absolute_url(self):
       return reverse('music:detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.title + '-' + self.artist



class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    title = models.CharField(max_length=250)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
