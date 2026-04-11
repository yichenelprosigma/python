def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])
my_list= [1,2,3,4,5,6]
print(sum_list(my_list))
#1.explicar la función , y dime los parámetros de cada vez cuando llama la función
#Significa que esta función desempeá la suma de todos los número de la lista pero tiene una condición base que es si es 0 la función siempre va dar cero pero si empieza por un número que no sea ni 0 puede empezar a suma
#Los parámetros que se usan son numbers y también se usa una lista llamada my_list