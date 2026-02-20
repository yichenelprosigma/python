#1.1 Filtrar números divisibles por 3 y 5
nums = [15, 22, 9, 30, 17, 6, 25]

divisibles = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, nums))

print(divisibles)

#Multiplicar elementos de la misma posición con map
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

resultado = list(map(lambda x, y: x * y, a, b))

print(resultado)

#Programa para calcular la media de cuatro valores

# Solicitar valores al usuario
v1 = float(input("Primer valor: "))
v2 = float(input("Segundo valor: "))
v3 = float(input("Tercer valor: "))
v4 = float(input("Cuarto valor: "))

# Calcular la media
media = (v1 + v2 + v3 + v4) / 4

print("La media es:", media)

