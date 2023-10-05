from django.db import models
from django.contrib.auth.models import User

 

class LostItem(models.Model):
    image = models.ImageField(upload_to='lost_items/')
    email = models.EmailField(unique=True, max_length=200, verbose_name='E-mail')
    name = models.CharField(max_length=200, verbose_name='Name')
    date_lost = models.DateField(max_length=200, verbose_name='Date Lost')
    location = models.CharField(max_length=200, verbose_name='Location')

    def __str__(self):
        return self.name

class FoundItem(models.Model):
    image = models.ImageField(upload_to='found_items/')
    email = models.EmailField(unique=True, max_length=200, verbose_name='E-mail')
    name = models.CharField(max_length=200, verbose_name='Name')
    date_found = models.DateField(max_length=200, verbose_name='Date Found')
    location = models.CharField(max_length=200, verbose_name='Location')

    def __str__(self):
        return self.name

class ClaimedItem(models.Model):
    image = models.ImageField(upload_to='claimed_items/')
    name = models.CharField(max_length=200, verbose_name='Name')

    def __str__(self):
        return self.name


class Item(models.Model):
    mage = models.ImageField(upload_to='found_items/')
    email = models.EmailField(unique=True, max_length=200, verbose_name='E-mail')
    name = models.CharField(max_length=200, verbose_name='Name')
    date = models.DateField(max_length=200, verbose_name='Date')
    date_found = models.DateField(max_length=200, verbose_name='Date Found')
    location = models.CharField(max_length=200, verbose_name='Location')
