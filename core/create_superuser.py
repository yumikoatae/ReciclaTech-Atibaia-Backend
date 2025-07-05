import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="admin",
        email="admin@email.com",
        password="senha123"
    )
    print("✅ Superusuário criado com sucesso.")
else:
    print("ℹ️ Superusuário já existe.")

