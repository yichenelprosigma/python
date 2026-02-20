#Lambda
#¿Qué es lambda en python?
# lambda es una función anónima
#una función normal
def suma():
    return 1+1 

#lambda argumentos:expresión
# lambda a: a+a
#x= lambda a, b , c: a+b-c

#¿Cuándo se usa lambda?
#1. Cuando mi función es muy simple o que se puede escribir en una línea
#2. para cuando hay una función de prueba 
#3. Cuando usamos tipo map, filter, sorted estos métodos, utilizamos lambda para programar
#se usaría la función

# a+b
# b+c
# c**2
# d+ c-b
# number=[1,2,3,4,5,6]
# for i in numbers:
#     print(numbers)

def main():
    # x=lambda a: a +2
    # print(x(5))

    # y= lambda a, b : a*b
    # print(y(1,2))
    
    #con método sorted
    # students=["Alice","Bob","Charlie","David"]
    # sorted_students= sorted(students, key=lambda x: len(x))
    # print(sorted_students)

    #con método map
    # numbers=[1,2,3,4,5]
    # squared= list(map(lambda x: x**2, numbers))
    # print(squared)
    
    #con método filter
    # numbers= [1,2,3,4,5,6,7,8,9,10]
    # evens= list(filter(lambda x: x % 2==0,numbers))
    # print(evens)

    # #doble lambda
    # multiply_by= lambda n: lambda x : x*n 



if __name__ == "__main__":
    main()

# tarea:
# 1. Escribir 3 lambda con 3 métodos con diferentes condiciones:
# 2. Escriba un programa que calcule la media de 4 valores introducidos por el usuario:
# primer valor:55
# segundo valor:99
# tercer valor:12
# cuarto valor: 32
# la media es : 45.62