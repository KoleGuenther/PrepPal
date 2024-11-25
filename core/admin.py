from django.contrib import admin
from .models import Recipe, FeaturedRecipe

class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['name']

class FeaturedRecipeAdmin(admin.ModelAdmin):
    list_display = ['recipe']
    autocomplete_fields = ['recipe']
    search_fields = ['recipe__name']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(FeaturedRecipe, FeaturedRecipeAdmin)
