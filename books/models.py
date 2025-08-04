from django.db import models
from datetime import date

# books/models.py
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    date_read = models.DateField(null=True, blank=True)  
    published_date = models.DateField(default=date.today)  
    description = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True)


    def __str__(self):
        return self.title
