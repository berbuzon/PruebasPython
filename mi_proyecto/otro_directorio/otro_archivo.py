import sys
import os

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Obtener la ruta absoluta del directorio del proyecto
project_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Agregar la ruta del proyecto al PYTHONPATH
sys.path.append(project_dir)

import ejemplo_paquete

resultado_suma=ejemplo_paquete.math_tools.sumar(10,5)
resultado_multiplicacion=ejemplo_paquete.operaciones.multiplicar(10,5)

print(f"Suma:{resultado_suma}")
print(f"Multiplicacion:{resultado_multiplicacion}")