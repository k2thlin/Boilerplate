from django.db import models

# Create your models here.
class Choice(models.Model):
    name= models.CharField(max_length=20)
    result = models.BooleanField(default= False)