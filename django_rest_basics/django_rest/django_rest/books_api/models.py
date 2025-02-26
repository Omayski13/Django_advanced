from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=20)
    page = models.IntegerField(default=0)
    description = models.TextField(max_length=100,default='')
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.title