from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    #CharField表示varchar
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    website = models.URLField()
    #URLField也是varchar，默认200

class Author(models.Model):
    name=models.CharField(max_length=20)
    age= models.IntegerField()
    email=models.EmailField(null=True)
    isactive=models.BooleanField(default=True)

class Book(models.Model):
    title=models.CharField(max_length=20)
    publicate_date=models.DateField()
