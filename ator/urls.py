from django.urls import path
from . import views

urlpatterns = [
    path('atores/', views.AtorCreateListView.as_view(), name='lista-cria-ator'),
    path('atores/<int:pk>/', views.AtorRetrieveUpdateDestroyView.as_view(), name='item-ator'),
]
