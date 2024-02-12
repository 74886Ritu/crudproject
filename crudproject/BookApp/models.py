from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=30)
    price=models.IntegerField()
    author=models.CharField(max_length=40)



# Create your models here.
