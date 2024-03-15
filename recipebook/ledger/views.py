from django.shortcuts import render
from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def recipe_list(request):
    ctx = { 'recipes': Recipe.objects.all() }
    return render(request, 'recipe_list.html', ctx)


def recipe_detail(request, id):
    ctx = { 
        'recipe': Recipe.objects.get(id=id), 
        'ingredient': Recipe.objects.get(id=id) }
    return render(request, 'recipe_detail.html', ctx)


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'