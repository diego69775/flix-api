from django.urls import path
from . import views

urlpatterns = [
    path('generos/', views.GeneroCreateListView.as_view(), name='lista-cria-genero'),
    path('generos/<int:pk>/', views.GeneroRetrivieveUpdateDestroyView.as_view(), name='item-genero'),
]
