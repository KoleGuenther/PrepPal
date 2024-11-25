from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Recipe, SavedRecipe, FeaturedRecipe
from .forms import RecipeForm, UserRegisterForm

# Main Page
def main_page(request):
    return render(request, 'core/main_page.html')

@login_required
def personal_recipes(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'core/personal_recipes.html', {'recipes': recipes})

# Create
@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'core/create_recipe.html', {'form': form})

# Read (List all)
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'core/recipe_list.html', {'recipes': recipes})

# Read (Single Recipe)
def view_recipe(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You must log in or create an account to view this recipe.')
        return redirect('login')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    saved_recipe = SavedRecipe.objects.filter(user=request.user, recipe=recipe).exists()

    context = {
        'recipe': recipe,
        'is_saved': saved_recipe,
    }
    return render(request, 'core/view_recipe.html', context)

# Update
def update_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'core/update_recipe.html', {'form': form, 'recipe': recipe})

# Delete
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'core/delete_recipe.html', {'recipe': recipe})

@login_required
def my_recipes(request):
    created_recipes = Recipe.objects.filter(user=request.user)
    saved_recipes = SavedRecipe.objects.filter(user=request.user)
    saved_recipe_ids = saved_recipes.values_list('recipe_id', flat=True)

    context = {
        'created_recipes': created_recipes,
        'saved_recipes': saved_recipes,
        'saved_recipe_ids': list(saved_recipe_ids),
    }
    return render(request, 'core/my_recipes.html', context)

@login_required
def toggle_save_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    saved_recipe = SavedRecipe.objects.filter(user=request.user, recipe=recipe).first()

    if saved_recipe:
        saved_recipe.delete()
    else:
        SavedRecipe.objects.create(user=request.user, recipe=recipe)
    return redirect(request.META.get('HTTP_REFERER', 'my_recipes'))

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

def featured_recipes(request):
    featured = FeaturedRecipe.objects.select_related('recipe')[:3] #3 Means that there will only be 3 recipes, change later if you want a bigger grid size (but for this scenario i dont wanna do extra work)
    return render(request, 'core/featured_recipes.html', {'featured_recipes': featured})