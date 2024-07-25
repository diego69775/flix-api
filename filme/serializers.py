from rest_framework import serializers
from filme.models import Filme
from django.db.models import Avg

class FilmeSerializer(serializers.ModelSerializer):
    media_nota = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Filme
        fields = '__all__'

    def get_media_nota(self, obj):
        nota = obj.reviews.aggregate(Avg('nota'))['nota__avg']

        if nota:
            return round(nota,1)
        return None
        

    def validate_data_lancamento(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1990.")
        return value
    
    def validate_resumo(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("Resumo não deve ser maior do que 200 caracteres.")
        return value