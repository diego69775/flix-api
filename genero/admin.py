from django.contrib import admin
from genero.models import Genero

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
