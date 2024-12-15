#!/usr/bin/env python3
import matplotlib.pyplot as plt

def line():
    # Datos
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Valores de x del 0 al 10
    y = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]  # Valores de y (cubos de x)

    # Crear la gráfica
    plt.plot(x, y, color='red', linestyle='-', label='y = x^3')  # Línea sólida roja

    # Etiquetas y título
    plt.xlabel('Eje x')  # Etiqueta del eje x
    plt.ylabel('Eje y')  # Etiqueta del eje y
    plt.title('Gráfica de y = x^3')  # Título

    # Definir límites del eje x
    plt.xlim(0, 10)

    # Mostrar la gráfica
    plt.legend()  # Mostrar la leyenda
    plt.grid(True)  # Activar la cuadrícula
    plt.show()

if __name__ == "__main__":
    line()