from rest_framework import viewsets
from .models import PostoDeColeta
from .serializers import PostoDeColetaSerializer

class PostoDeColetaViewSet(viewsets.ModelViewSet):
    queryset = PostoDeColeta.objects.all()
    serializer_class = PostoDeColetaSerializer

