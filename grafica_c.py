import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 1. Crear los datos para los ejes X e Y (rango más amplio para ver el comportamiento)
x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)

# 2. Calcular el argumento del logaritmo: (x^2 + y^2 - 1)
argumento = X**2 + Y**2 - 1

# 3. Aplicar una máscara matemática: solo calcular donde el argumento sea estrictamente mayor que 0
# Reemplazamos los valores inválidos con NaN (Not a Number) para que Matplotlib no los grafique
Z = np.where(argumento > 0, np.log(argumento), np.nan)

# 4. Configurar la figura y el entorno 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 5. Dibujar la superficie de la gráfica
# Usamos el mapa de color 'viridis' para resaltar los cambios de altura
superficie = ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none', rstride=1, cstride=1)

# 6. Personalizar etiquetas, límites y títulos
ax.set_title('Vista Isométrica $f(x,y) = \ln(x^2 + y^2 - 1)$', fontsize=18, fontweight='bold')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Ajustamos el límite en Z porque la función tiende a menos infinito cerca del radio = 1
ax.set_zlim(-4, 3) 

# 7. Añadir la barra de color lateral
#fig.colorbar(superficie, ax=ax, shrink=0.5, aspect=5)

# 8. Mostrar la gráfica interactiva en pantalla

# Opciones alternativas (descomenta la que quieras usar):
# ax.view_init(elev=0, azim=-90)    # Para Vista FRONTAL (Eje X y Eje Z)
# ax.view_init(elev=0, azim=0)      # Vista LATERAL DERECHA (Eje Y y Eje Z)
# ax.view_init(elev=90, azim=-90)   # Vista SUPERIOR / PLANTA (Eje X y Eje Y)
# ax.view_init(elev=30, azim=45)     # Vista ISOMÉTRICA (Por defecto)
plt.show()
