from django.db import models
from datetime import date

class Book(models.Model):
    title = models.CharField(max_length=200, default='Untitled Book')
    author = models.CharField(max_length=100, default='Unknown Author')
    cover_pic = models.ImageField(upload_to='cover_pics/', blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True, default='0000000000000')
    description = models.TextField(default='No description available')
    category = models.CharField(max_length=50, default='General')
    published_date = models.DateField(default=date.today)
    available_copies = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title


