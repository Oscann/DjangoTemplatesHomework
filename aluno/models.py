from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    cpf = models.CharField(max_length=14)
    data_de_nascimento = models.DateField()

    def __str__(self):
        return self.nome