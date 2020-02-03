from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250,unique_for_date='date')
    description = models.TextField()
    description.label = None
    date = models.DateField()
    def __str__(self):
        return self.title
