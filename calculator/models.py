from django.db import models

# Create your models here.
class Equation(models.Model):
    equation_string = models.TextField()