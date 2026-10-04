import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 1. Crear los datos para los ejes X e Y (-5 a 5 con buena resolución)
x = np.linspace(-5, 5, 300)
y = np.linspace(-5, 5, 300)
X, Y = np.meshgrid(x, y)

# 2. Calcular el argumento dentro de la raíz: (x^2 - y^2)
argumento = X**2 - Y**2

# 3. Aplicar una máscara matemática: solo calcular la raíz donde el argumento sea >= 0
# Los valores negativos se reemplazan con NaN (Not a Number) para que no se grafiquen
Z = np.where(argumento >= 0, np.sqrt(argumento), np.nan)

# 4. Configurar la figura y el entorno 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 5. Dibujar la superficie de la gráfica
# Usamos el mapa de color 'terrain' o 'coolwarm' para resaltar el relieve matemático
superficie = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', rstride=1, cstride=1)

# 6. Personalizar etiquetas y títulos
ax.set_title('Vista Isométrica $f(x,y) = \sqrt{x^2 - y^2}$', fontsize=18, fontweight='bold')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Ajustar los límites de visualización
ax.set_zlim(0, 5)

# 7. Añadir la barra de color lateral
#fig.colorbar(superficie, ax=ax, shrink=0.5, aspect=5)

# 8. Mostrar la gráfica interactiva

# Opciones alternativas (descomenta la que quieras usar):
# ax.view_init(elev=0, azim=-90)    # Para Vista FRONTAL (Eje X y Eje Z)
# ax.view_init(elev=0, azim=0)      # Vista LATERAL DERECHA (Eje Y y Eje Z)
# ax.view_init(elev=90, azim=-90)   # Vista SUPERIOR / PLANTA (Eje X y Eje Y)
# ax.view_init(elev=30, azim=45)     # Vista ISOMÉTRICA (Por defecto)
plt.show()
