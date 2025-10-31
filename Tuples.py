#create a tuple
my_tuple= (1, 2, 3, 4, 5)

print(my_tuple)

print(my_tuple[0])

#create a tuple with different data.
mixed_tuple=(10,"hello",9,99,True)
print(mixed_tuple)

tuple1=(1,)

#tuple auto
tuple2=(1,2,3)
print(type(tuple2))

# error of tuple, can not modify
# my_tuple[0]=10
# print(my_tuple[0])

print(my_tuple[1:3])

#methods of tuple
tuple3=(1,2,3,4,2,3,2)
#count()
print(tuple3.count(2))

#index()
print(tuple3.index(3))

# desempaquetado de tuplas
tuple_person=("Lilia",1999,"Madrid")
name, year, country=tuple_person

print("My name is", name, ", I was born in", year, "in", country, ".")

#the use of tuple
color_rgb=(255,0,0) #red color

month=("January","February","March","April","May","June","July","August","September","October","November","December")

#convert tuple to list
list_color_rgb=list(color_rgb)
#Exercise 01:
#Tienes una tupla que contiene información sobre un estudiante:
estudiantes=(
    ("Ana",(8,9,10)),
    ("Luis",(7,6,9)),
    ("Maria",(10,10,9)
))
#1 calcula el promedio de cada estudiante y muestra su nombre junto con el promedio.
#2 Encontrar esudiante con el promedio más alto en el tercercuatrimeste y mostrar su nombre y promedio

#Exercise 02:
# Desempaquetar la tupla
datos=("Madrid",2025,(28.3, -16.6))
#con 3 lineas de codigo

