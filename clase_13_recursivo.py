#for i in range(5):
#   print(i)

# ejemplo 1:
def countdown(n):
    if n <= 0:
        print("Donel")
    else:
        print(n)
        countdown(n-1)
countdown(10)

# ejemplo 2: factoria de un número
def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
# 5 * 4 * 3 * 2 *1

def fibonacci (n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci (n-2)

print(fibonacci(7))

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])
my_list= [1,2,3,4,5,6]
print(sum_list(my_list))
#1.explicar la función , y dime los parámetros de cada vez cuando llama la función
# problema6.py
# Tarea: Desarrolle en python un programa que reciba como entrada las longitudes de los dos catetos de un
# triángulo rectángulo, y que calcule como salida la longitud de la hipotenusa del triángulo, dado por el
# teorema de Pitágoras. Necesitará para ello math.sqrt(), import math (importacion de la libreria)
# Introduzca cateto a: 7
# Introduzca cateto b: 5 
# El valor de la hipotenusa es 8.60

# c1 ^ 2 + c2 ^ 2 = hipo ^ 2