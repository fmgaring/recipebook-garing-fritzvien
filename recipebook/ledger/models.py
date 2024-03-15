from django.db import models
from django.urls import reverse


# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:detail', args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    author = models.CharField(max_length=50)

    created_on = models.DateTimeField(auto_now_add=True)

    update_on = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:detail', args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe")
    
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients")
    
