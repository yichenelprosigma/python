i = 1
suma = 0

while i <= 100:
    suma += i
    i += 1

print(suma)

password_correct = "123456"
password = ""

while password != password_correct:
    password = input("Introduzca la contraseña:")
    if(password != password_correct):
        print("Contraña incorrecta, vuelva a intentarlo")

print("Contraseña correcta")

# NameError: name 'true' is not defined
# corregido 
while True:
    print("hello world")


numero = int(input("Introduce un número para calcular su factorial: "))

resultado = 1  
i = 1           

while i <= numero:
    resultado *= i  
    i += 1            

print("El factorial es:", resultado)
a = 0
b = 1

while a <= 100:
    print(a)
    c = a + b
    a = b
    b = c
num = int(input("Introduce un número: "))
i = 1

print("Divisores:")

while i <= num:
    if num % i == 0:
        print(i)
    i += 1
