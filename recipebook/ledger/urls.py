from django.urls import path
from .views import recipes_list, recipe1, recipe2

urlpatterns = [
    path('recipes/list', recipes_list, name='list'),
    path('recipe/1', recipe1, name='1'),
    path('recipe/2', recipe2, name='2'),
]

app_name = 'ledger'