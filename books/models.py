from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    book_image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + '-' + self.author

    def get_absolute_url(self):
        return reverse('books:detail', args=[str(self.id)])