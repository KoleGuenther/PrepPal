from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipe/new/', views.create_recipe, name='create_recipe'),
    path('recipe/<int:recipe_id>/', views.view_recipe, name='view_recipe'),
    path('recipe/<int:pk>/edit/', views.update_recipe, name='update_recipe'),
    path('recipe/<int:pk>/delete/', views.delete_recipe, name='delete_recipe'),
    path('my_recipes/', views.my_recipes, name='my_recipes'),
    path('featured', views.featured_recipes, name='featured_recipes'),
    path('toggle-save/<int:recipe_id>/', views.toggle_save_recipe, name='toggle_save_recipe'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]