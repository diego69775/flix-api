from django.db import models
from filme.models import Filme
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    filme = models.ForeignKey(
        Filme, 
        on_delete=models.PROTECT,
        related_name='reviews')
    nota = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas.'),
        ]
    )
    comentario = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.filme)