from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from coleta.views import PostoDeColetaViewSet

router = DefaultRouter()
router.register(r'postos', PostoDeColetaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]

