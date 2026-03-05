import math
#1.explicar la función , y dime los parámetros de cada vez cuando llama la función
# problema6.py
# Tarea: Desarrolle en python un programa que reciba como entrada las longitudes de los dos catetos de un
# triángulo rectángulo, y que calcule como salida la longitud de la hipotenusa del triángulo, dado por el
# teorema de Pitágoras. Necesitará para ello math.sqrt(), import math (importacion de la libreria)
# Introduzca cateto a: 7
# Introduzca cateto b: 5 
# El valor de la hipotenusa es 8.6
cateto_a=int(input("Dime un número para el cateto A "))
cateto_b=int(input("Dime un número para el cateto B "))
def geometría(cateto_a,cateto_b):
    resultado=math.sqrt(cateto_a**2+cateto_b**2)
    print("El valor de la hipotenusa es", round(resultado,1))
geometría(cateto_a,cateto_b)