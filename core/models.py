from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    short_desc = models.TextField(max_length=200)
    image = models.ImageField(upload_to='', null=True, blank=True)
    ingredients = models.TextField()
    instructions= models.TextField()
    cook_time = models.PositiveIntegerField()
    is_quick_meal = models.BooleanField(default=False)
    is_limited_appliances = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SavedRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} saved {self.recipe.title}"
    
class FeaturedRecipe(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, related_name='featured')

