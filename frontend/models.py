from django.db import models

# Create your models here.
class PostItem(models.Model):
    itemID     = models.CharField(max_length=255) # Svarer til feltet ID
    itemnumber = models.CharField(max_length=255) # Svarer til feltet Varenummer
    name       = models.CharField(max_length=255) # Svarer til feltet Navn