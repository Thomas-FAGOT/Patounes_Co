from django.db import models

class Animal(models.Model):
    name=models.fields.CharField(max_length=100)
    age=models.fields.CharField(max_length=100)
    localisation=models.fields.CharField(max_length=100)
    resume=models.fields.CharField(max_length=300)
    favorite=models.BooleanField()