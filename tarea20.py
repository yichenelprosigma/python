def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])
my_list= [1,2,3,4,5,6]
print(sum_list(my_list))
#1.explicar la función , y dime los parámetros de cada vez cuando llama la función
#Una iteracción 