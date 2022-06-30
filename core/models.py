import email
from django.db import models
from django.forms import EmailField

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return self.name