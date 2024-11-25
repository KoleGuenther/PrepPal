from django import forms
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'short_desc', 'ingredients', 'instructions', 'cook_time', 'is_quick_meal', 'is_limited_appliances', 'is_vegetarian']