from django.db import models

# Create your models here.
class Destination(models.Model):

    name= models.CharField(max_length=100)
    upload_picture = models.ImageField(upload_to='pics')
    upload_card = models.ImageField(upload_to='pics')