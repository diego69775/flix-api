from django.urls import path
from . import views

urlpatterns = [
    path('filmes/', views.FilmeCreateListView.as_view(), name='lista-cria-filme'),
    path('filmes/<int:pk>/', views.FilmeRetrieveUpdateDestroyView.as_view(), name='item-filme'),
]
