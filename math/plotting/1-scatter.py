#!/usr/bin/env python3
import matplotlib.pyplot as plt

# Datos
x = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]  # Altura en pulgadas
y = [150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]  # Peso en libras

# Crear la gráfica de dispersión
plt.scatter(x, y, color='magenta', label="Men's Height vs Weight")

# Etiquetas y título
plt.xlabel('Height (in)')  # Etiqueta del eje x
plt.ylabel('Weight (lbs)')  # Etiqueta del eje y
plt.title("Men's Height vs Weight")  # Título

# Mostrar la gráfica
plt.legend()  # Mostrar la leyenda
plt.grid(True)  # Activar la cuadrícula
plt.show()