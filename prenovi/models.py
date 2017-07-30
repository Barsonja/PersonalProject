from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
import uuid

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Enter your text here')
    date = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse('post-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.title


class Contractor(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    work = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse('contractor-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.last_name + ' ' + self.name

def get_end_date():
    return datetime.today() + timedelta(days=30)


class WorkInstance(models.Model):
    client_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, help_text="Name of the project")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular workinstance  across whole Database")
    contractor = models.ForeignKey('Contractor', null=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField(default=datetime.today())
    end_date = models.DateTimeField(default=get_end_date)
    summary = models.TextField(max_length=1000, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('workinstance-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.title + ', ' + self.client_name

