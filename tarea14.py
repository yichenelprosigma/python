num = int(input("Introduce un número: "))

if num > 0 and num % 2 == 0 and num % 3 != 0:
    print("Cumple las condiciones")
else:
    print("No cumple las condiciones")
#tarea 2
lista = [2, -1, -5, -8, 10, 45, 8, 92]
positivo = True

for num in lista:
    if num <= 0:
        positivo = False

if positivo:
    print("Todos los números son positivos")
else:
    print("No todos los números son positivos")
#tarea 3
edad = int(input("Edad: "))
sexo = input("Sexo: masculino o femenino: ")

if edad >= 18 and sexo == "masculino":
    print("Puede entrar")
else:
    print("No puede entrar")
#tarea 4
# numero = int(input("Introduce un número: "))

# if numero % 3 == 0 and numero % 5 == 0:
#     print("Es múltiplo de 3 o de 5")
# else:
#     print("No es múltiplo de 3 ni de 5")

# numero = int(input("Introduce un número: "))

# if numero % 3 == 0 and numero % 5 == 0:
#     for num1 in range(numero):
#         if num1 != 0:
#             if numero % num1 == 0:
#                 print("los divisores del número", num1)

# else:
#     print("No es múltiplo de 3 ni de 5")

#tarea 2
# lista = [2, -1, -5, -8, 10, 45, 8, 92]
# positivo = True
# suma=0
# for num in lista:
#     if num <= 0:
#         print(num)
#     else:
#         suma+=num
    
        
        

# if positivo:
#     print("Todos los números son positivos")
# else:
#     print("No todos los números son positivos")
