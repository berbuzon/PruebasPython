# filepath: /c:/Users/Bernardo/Documents/PruebasPython/mi_proyecto/main.py
import sys
import os

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Obtener la ruta absoluta del directorio del proyecto
project_dir = os.path.abspath(os.path.join(current_dir, '.'))

# Agregar la ruta del proyecto al PYTHONPATH
sys.path.append(project_dir)

# Importar y ejecutar otro_archivo.py
from otro_directorio import otro_archivo