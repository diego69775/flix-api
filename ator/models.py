from django.db import models

#TUPLA (valores não pode repetidos) - Usado para definir que no campo nacionalidade seja somente os campos que eu definir.
NACIONALIDADE_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
)

class Ator(models.Model):
    name = models.CharField(max_length=200)
    data_nascimento = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(
        max_length=100,
        choices=NACIONALIDADE_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name