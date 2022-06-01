from django.db import models

# Create your models here.
class PostItem(models.Model):
    name =  models.CharField(max_length=255) # Svarer til feltet Navn