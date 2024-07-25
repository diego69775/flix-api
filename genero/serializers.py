from rest_framework import serializers
from genero.models import Genero

class GeneroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genero
        #Retornar todos os campos da class Genero
        fields = '__all__'
        #Caso eu queira que mostra apenas um campo especifico fazer uma lista
        #fields = ['name']