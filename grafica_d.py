import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 1. Crear los datos para los ejes X e Y (-4 a 4 con alta resolución)
x = np.linspace(-4, 4, 200)
y = np.linspace(-4, 4, 200)
X, Y = np.meshgrid(x, y)

# 2. Definir la función matemática f(x,y) = sin(x * y)
Z = np.sin(X * Y)

# 3. Configurar la figura y el entorno 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 4. Dibujar la superficie de la gráfica
# Usamos 'viridis' o 'bwr' para diferenciar claramente las crestas de los valles
superficie = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none', rstride=2, cstride=2)

# 5. Personalizar etiquetas y títulos
ax.set_title('Vista Isométrica $f(x,y) = \sin(xy)$', fontsize=18, fontweight='bold')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z / f(x,y)')

# El eje Z siempre oscilará estrictamente entre -1 y 1
ax.set_zlim(-1.5, 1.5)

# 6. Añadir la barra de color lateral
#fig.colorbar(superficie, ax=ax, shrink=0.5, aspect=5)

# 7. Mostrar la gráfica interactiva

# Opciones alternativas (descomenta la que quieras usar):
# ax.view_init(elev=0, azim=-90)    # Para Vista FRONTAL (Eje X y Eje Z)
# ax.view_init(elev=0, azim=0)      # Vista LATERAL DERECHA (Eje Y y Eje Z)
# ax.view_init(elev=90, azim=-90)   # Vista SUPERIOR / PLANTA (Eje X y Eje Y)
# ax.view_init(elev=30, azim=45)     # Vista ISOMÉTRICA (Por defecto)
plt.show()
