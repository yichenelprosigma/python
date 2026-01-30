#¿para que sirve una función?
#función sirve para reutilizar los códigos

# a=10
# b=5

# print(a+b)

# c=1
# d=2

# print(c+d)

# e= -1
# f=-5
# print(e+f)
#definir variables
a=10
b=5
#implementación de la función suma

#def= definición
#suma = nombre de la función
#valor 1= primer parámetro
#valor 2= segundo parámetro
def suma(valor1, valor2):
    print(valor1+valor2)

#llamada de la función suma
suma(a,b)
suma(4,10)

#implementación de la función helloworld
def say_hello():
    print("hello world")
say_hello()

# la diferencia entre print vs return

def suma2(valor1,valor2):
    return valor1 + valor2

resultado=suma2(10,10)*2
print(resultado)

#cualquiar cosa que está después de return no hace nada
def test():
    return 10

#hacer la potencia 2 de un numero, parametros es valor1
def square(valor1):
    return valor1 * valor1

print(square(5))

year_of_born=int(input("Introduzca tu año de nacimiento:"))
actualYear= int(input("¿El año actual?"))

def calcuteAge(year_of_born,actualyear):
    age=actualYear-year_of_born
    print("Año de nacimiento:", year_of_born)
    print("Año actual:", actualyear)
    print("Su edad es", age ,"años")
calcuteAge(year_of_born,actualYear)