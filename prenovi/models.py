from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Enter your text here')
    date = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse('post-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.title
