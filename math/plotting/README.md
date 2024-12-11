PLOTING :

¿Qué es un gráfico (plot)?
Un gráfico o plot es una representación visual de datos, diseñada para facilitar su análisis y comprensión. Los gráficos permiten observar patrones, tendencias y relaciones entre variables, algo que a veces resulta difícil de identificar en tablas de datos numéricos.
Ejemplo: Si tienes datos sobre las temperaturas diarias durante un mes, un gráfico puede mostrar cómo cambian las temperaturas día a día de manera clara y visual.

¿Qué es un gráfico de dispersión (scatter plot)?
Un gráfico de dispersión muestra puntos individuales en un plano cartesiano. Cada punto representa un par de valores (x, y), que corresponden a dos variables diferentes.Se usa comúnmente para analizar la relación entre dos variables y observar patrones, como correlaciones positivas, negativas o la ausencia de relación.

- Eje X: Representa la primera variable.
- Eje Y: Representa la segunda variable.
  Ejemplo: Relación entre la cantidad de horas de estudio y la calificación obtenida en un examen.
  Código de ejemplo con Matplotlib:

          import matplotlib.pyplot as plt

          # Datos
          x = [1, 2, 3, 4, 5]
          y = [2, 4, 1, 8, 7]

          # Crear gráfico de dispersión
          plt.scatter(x, y)
          plt.title('Gráfico de dispersión')
          plt.xlabel('Horas de estudio')
          plt.ylabel('Calificación')
          plt.show()

¿Qué es un gráfico de líneas (line graph)?
Un gráfico de líneas conecta puntos de datos mediante líneas. Es ideal para representar cambios continuos a lo largo del tiempo u otras variables. Este tipo de gráfico se utiliza mucho en series temporales.
Ejemplo: Mostrar cómo cambia la temperatura durante una semana.
Código de ejemplo:

        # Datos

        dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        temperaturas = [20, 22, 21, 19, 23]

        # Crear gráfico de líneas

        plt.plot(dias, temperaturas)
        plt.title('Temperaturas semanales')
        plt.xlabel('Días')
        plt.ylabel('Temperatura (°C)')
        plt.show()

¿Qué es un gráfico de barras (bar graph)?
Un gráfico de barras representa datos categóricos mediante barras. La longitud o altura de cada barra muestra la cantidad o frecuencia de la categoría correspondiente.
Ejemplo: Comparar las ventas de diferentes productos en un mes.
Código de ejemplo:

        # Datos

        productos = ['A', 'B', 'C', 'D']
        ventas = [100, 150, 80, 120]

        # Crear gráfico de barras

        plt.bar(productos, ventas)
        plt.title('Ventas por producto')
        plt.xlabel('Productos')
        plt.ylabel('Ventas')
        plt.show()

¿Qué es un histograma?
Un histograma es similar a un gráfico de barras, pero se utiliza para representar la distribución de datos continuos. Agrupa los datos en intervalos (bins) y muestra cuántos valores caen en cada intervalo.
Ejemplo: Distribución de edades de un grupo de personas.
Código de ejemplo:

        # Datos

        edades = [22, 25, 25, 30, 30, 35, 40, 40, 45, 50]

        # Crear histograma

        plt.hist(edades, bins=5, edgecolor='black')
        plt.title('Distribución de edades')
        plt.xlabel('Rango de edades')
        plt.ylabel('Frecuencia')
        plt.show()

¿Qué es Matplotlib?
Matplotlib es una biblioteca de Python que permite crear gráficos de alta calidad de forma sencilla. Es una de las herramientas más populares para la visualización de datos en Python.Su módulo principal, matplotlib.pyplot, ofrece funciones similares a las de MATLAB, pero adaptadas para Python.

Cómo graficar datos con Matplotlib

1.  Importar la biblioteca:python
2.  import matplotlib.pyplot as plt
3.  Definir datos:Define los valores que quieres graficar, como listas o arrays.
4.  Elegir el tipo de gráfico:Usa funciones como plt.plot(), plt.scatter(), plt.bar(), etc.
5.  Mostrar el gráfico:Usa plt.show() para visualizar el gráfico.
    Ejemplo básico:

         x = [1, 2, 3, 4]
         y = [2, 4, 6, 8]

         plt.plot(x, y)
         plt.title('Ejemplo básico')
         plt.xlabel('Eje X')
         plt.ylabel('Eje Y')
         plt.show()

Cómo etiquetar un gráfico
Para añadir etiquetas a un gráfico, puedes usar las siguientes funciones:

- plt.title(): Agrega un título al gráfico.
- plt.xlabel(): Etiqueta el eje X.
- plt.ylabel(): Etiqueta el eje Y.
  Ejemplo:

        plt.plot(x, y)
        plt.title('Gráfico etiquetado')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.show()

Cómo escalar un eje
Puedes ajustar los límites de los ejes utilizando:

- plt.xlim(min, max): Ajusta el rango del eje X.
- plt.ylim(min, max): Ajusta el rango del eje Y.
  Ejemplo:

        plt.plot(x, y)
        plt.xlim(0, 5)
        plt.ylim(0, 10)
        plt.show()

Cómo graficar múltiples conjuntos de datos al mismo tiempo
Para mostrar más de un conjunto de datos en el mismo gráfico, simplemente realiza varias llamadas a la función plt.plot() antes de usar plt.show(). También puedes añadir una leyenda con plt.legend().
Ejemplo:

        x = [1, 2, 3, 4]
        y1 = [2, 4, 6, 8]
        y2 = [1, 3, 5, 7]

        plt.plot(x, y1, label='Conjunto 1')
        plt.plot(x, y2, label='Conjunto 2')

        plt.title('Gráfico con múltiples conjuntos')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.legend()
        plt.show()
