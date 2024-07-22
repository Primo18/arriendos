# scripts/consultas.py

import os
import sys
import django

# Agrega el directorio del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Establece la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arriendos.settings")

# Configura Django
django.setup()

from inmuebles.models import Inmueble

# Realiza la consulta
inmuebles = Inmueble.objects.filter(comuna__nombre="Santiago").values(
    "nombre", "descripcion"
)
with open("inmuebles_santiago.txt", "w") as file:
    for inmueble in inmuebles:
        file.write(f"{inmueble['nombre']}: {inmueble['descripcion']}\n")
