from django.db import models

# Create your models here.

class movies (models.Model):
    name: models.CharField(max_length=50, null=False)
    year: models.IntegerField(max_length=4, null=False)
    director: models.CharField(max_length=30, null=False)
    gender: models.CharField(max_length=10, null=False)
    synopsis: models.TextField(max_length=70, null=False)
    
    def __str__(self) -> str:
        return self.name    
    
