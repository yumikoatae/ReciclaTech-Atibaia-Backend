from django.db import models

class PostoDeColeta(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    horario_funcionamento = models.CharField(max_length=100)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return self.nome

