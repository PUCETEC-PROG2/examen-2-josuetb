from django.contrib import admin

from .models import movies

# Register your models here.
@admin.register(movies)
class moviesAdmin(admin.ModelAdmin):
    pass