from rest_framework import serializers
from .models import PostoDeColeta

class PostoDeColetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostoDeColeta
        fields = '__all__'

