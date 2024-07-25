from django.contrib import admin
from ator.models import Ator

@admin.register(Ator)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'data_nascimento', 'nacionalidade')
