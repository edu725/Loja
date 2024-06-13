from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class  Livro(models.Model):
    titulo = models.CharField(max_length=240)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="imagens/")


class Curtida(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

class Comentarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    conteudo = models.TextField()
