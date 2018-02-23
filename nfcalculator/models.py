from django.db import models
from django.contrib.auth.models import User


class NutritionFact(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)


class Allergen(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)


class Extra(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)


class Ingredient(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=False)
    allergens = models.ManyToManyField(Allergen)
    may_contain = models.ManyToManyField(Extra)


class Product(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)


class ProductIngredient(models.Model):
    product = models.ForeignKey(Product)
    ingredient = models.ForeignKey(Ingredient)
    weight = models.FloatField(null=False, default=0)


class IngredientNutritionFact(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    nutrition_fact = models.ForeignKey(NutritionFact)
    weight = models.FloatField(null=False, default=0)
