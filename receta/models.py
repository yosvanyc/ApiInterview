# from django.contrib.auth.models import User
from django.db import models

from user.models import User
# Create your models here.


class Receta(models.Model):

    name = models.CharField(max_length=50, null=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Return name of receta"""
        return self.name


class Step(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)

    step_text = models.TextField(max_length=500, null=False)

    def __str__(self):
        """Return name of receta"""
        return self.receta.name


class Ingredient(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)

    text = models.CharField(max_length=50, null=False)

    def __str__(self):
        """Return name of receta"""
        return self.receta.name
