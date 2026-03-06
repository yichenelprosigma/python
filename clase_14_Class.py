# Class 
#1. dentro de una clase hay varios atributos(variable) y métodos(funciones).


# Cómo se define una class
# class NombreDeLaClase:
#     atributos
#     métodos


# Ejemplos:
# Creación de una clase en python
# class MyClass:
#     crear un atributo en la clase
#     x=5

# La llamada de la class
# Primero tenemos que crear un objeto de la class de MyClass, y luego utilizar "cosas" de la clase
# obj=MyClass()
# print(obj.x)

# -------------------------------------------------------------------------------------------------------------------- #

# El uso de _init_()
# Ejemplo:
# class Person:
#     def __init__(self, name, age): 
#         self.name= name
#         self.age=age
#         print(f"Acabas de crear un objeto persona : {self.name}, con edad de {self.age}")
# p1= Person("Juan", 18)

# p2= Person("Ana", 20)

# print(p1.name)
# print(p2.age)

#falla por que falta un argumento de la clase
# p3=Person("Julián")

# # --------------------------------------------------------------------------------------------------------------------- #
# clase de estudiante 
class Student:
    def __init__(self, name="Nameless", age="-", claseStudent="X"):
        self.name =name
        self.age= age
        self.claseStudent=claseStudent
        print(f"Create a new student with name: {self.name} , with age {self.age}, in class {self.claseStudent}")

# Crear un objeto sin parámetros
student1=Student()
print(student1.name)
print(student1.age)
print(student1.claseStudent)

#Crear un objeto con parámetros 
student2= Student("Lilia",26,"A")
print(student2.name)
print(student2.age)
print(student2.claseStudent)

# # -------------------------------------------------------------------------------------------------------------------------- #

# Crear una clase con métodos
class Cat:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    # Métodos 
    def meowing(self):
        return f"{self.name} dice: miao miao "
    def correr(self, Energía):
        # cuando corre cada 3s, energía -10
        # cuando energía =< 0
        pass

obj_cat= Cat("Ryke", 5)
print(obj_cat.meowing())




































































































































































