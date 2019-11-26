from django.db import models

# Create your models here.

class Genero(models.Model):
    nm_genero = models.CharField(verbose_name="Gênero",max_length=10)
    sg_genero = models.CharField(verbose_name="Abrev. gênero",max_length=4)



class Cliente(models.Model):
    nome = models.CharField(verbose_name="Nome",max_length=45)
    cpf = models.CharField(verbose_name="CPF",max_length=14)
    fk_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name= "Gênero", default=0)
    telefone = models.CharField(verbose_name="Telefone",max_length=14)
    idade = models.IntegerField(verbose_name="Idade")
