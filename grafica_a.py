import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Crear los datos para los ejes X e Y (-5 a 5)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 2. Definir la función matemática f(x,y)  = x^2  + y^2
Z = X**2 + Y**2

# 3. Configurar la figura y el entorno 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 4. Dibujar la superficie de la gráfica
ax.plot_surface(X, Y, Z, cmap='viridis')

# Set the view angle for an isometric view
ax.view_init(elev=30, azim=-45)

# 5. Personalizar etiquetas y títulos
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Vista Isométrica $f(x,y)= x^2 + y^2$', fontsize=18, fontweight='bold')

# 7. Mostrar la gráfica interactiva
# Opciones alternativas (descomenta la que quieras usar):
# ax.view_init(elev=0, azim=-90)    # Para Vista FRONTAL (Eje X y Eje Z)
# ax.view_init(elev=0, azim=0)      # Vista LATERAL DERECHA (Eje Y y Eje Z)
# ax.view_init(elev=90, azim=-90)   # Vista SUPERIOR / PLANTA (Eje X y Eje Y)
# Sax.view_init(elev=30, azim=45)     # Vista ISOMÉTRICA (Por defecto)
plt.show()