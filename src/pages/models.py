from django.db import models

# Create your models here.
# models.py is where we define our database models, 
# which Django automatically translates into database tables

class MealPlan(models.Model):
    title = models.CharField(max_length = 75)
    calories = models.IntegerField()