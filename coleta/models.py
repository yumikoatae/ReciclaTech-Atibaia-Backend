from django.db import models
from geopy.geocoders import Nominatim
from django.core.exceptions import ValidationError

class PostoDeColeta(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    horario_funcionamento = models.CharField(max_length=100)
    feedback = models.TextField(blank=True)

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Só tenta buscar se ainda não tem coordenadas
        if (not self.latitude or not self.longitude) and self.endereco:
            geolocator = Nominatim(user_agent="reciclatech")
            location = geolocator.geocode(self.endereco)
            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude
            else:
                raise ValidationError("Endereço não encontrado para geocodificação.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

