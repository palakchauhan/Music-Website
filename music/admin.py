
# Register your models here.
from django.contrib import admin
from .models import Album, Song

admin.register(Album)(admin.ModelAdmin)
admin.register(Song)(admin.ModelAdmin)