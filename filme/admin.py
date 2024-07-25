from django.contrib import admin
from filme.models import Filme

@admin.register(Filme)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'genero', 'data_lancamento', 'resumo')
