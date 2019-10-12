from django.db import models


# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    description = models.TextField()
    image = models.FilePathField(path="/img")
