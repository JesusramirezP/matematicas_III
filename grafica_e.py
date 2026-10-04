import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 1. Crear los datos para los ejes X e Y (-5 a 5)
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)

# 2. Definir la función original controlando la división por cero
# Ponemos una condición: si x es muy cercano a y, asignamos NaN (no se grafica)
tolerancia = 0.05
Z = np.where(np.abs(X - Y) > tolerancia, (X**2 - Y**2) / (X - Y), np.nan)

# 3. Configurar la figura y el entorno 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 4. Dibujar la superficie de la gráfica
# Usamos 'coolwarm' para ver la inclinación del plano de abajo hacia arriba
superficie = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# 5. Personalizar etiquetas y títulos
ax.set_title('Vista Lateral Derecha $f(x,y) = \\frac{x^2 - y^2}{x - y}$', fontsize=18, fontweight='bold')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# 6. Añadir la barra de color lateral
#fig.colorbar(superficie, ax=ax, shrink=0.5, aspect=5)

# 7. Mostrar la gráfica interactiva

# Opciones alternativas (descomenta la que quieras usar):
# ax.view_init(elev=0, azim=-90)    # Para Vista FRONTAL (Eje X y Eje Z)
ax.view_init(elev=0, azim=0)      # Vista LATERAL DERECHA (Eje Y y Eje Z)
# ax.view_init(elev=90, azim=-90)   # Vista SUPERIOR / PLANTA (Eje X y Eje Y)
# ax.view_init(elev=30, azim=45)     # Vista ISOMÉTRICA (Por defecto)
plt.show()
