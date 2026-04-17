# # Tema: Herencia
# # Concepto: En la POO(programación orientada a objetos), es compartir atributos (variables) y métodos (funciones) entre clases

# # crear una instancia o objeto

# # Class padre= Animal
# # Clases hijos= Perro, Gato, León, Panda, Oveja...

# # Paso 1: Definir una clase padre
# class Animal:
#     def speak(self):
#         print("Animal make sounds")

# #Paso 2: Crear una clase hijo
# class Dog():
#     pass

# # Crear 3: un objeto de la clase perro
# dog1= Dog()
# dog1.speak()

# class Student:
#     #constructor de la clase cuando se crea el hace todo
#     def __init__(self):
#         self.name=name
        
# estudiante1= Student("Juan")
# print(estudiante1.name)

# Constructor por defecto y constructor definido

# ejemplo de clase heredada:
class Person:
    def __init__(self,name, lastname, age):
        self.name=name
        self.lastname=lastname
        self.age=age
    def showInfo(self):
        txt= "full name= {0} {1}, age= {2}"
        return txt.format(self.name,self.lastname,self.age)


class Student(Person):
    def __init__(self, name, lastname, age, degree):
        #se refiere la clase padre 
        super().__init__(name, lastname, age)
        self.degree = degree

class profesional(Person):
    def __init__(self, name, lastname, age, profesion):
        super().__init__(name, lastname, age)
        self.profesion= profesion
class deportista(Person):
    def __init__(self, name, lastname, age, deporte):
        super().__init__(name, lastname, age)
        self.deporte=deporte
class Futbolist(deportista):
    def __init__(self, name,lastname, age, team):
        super().__init__(name,lastname, age, "futbol")
        self.team=team

#instacia=objeto de la clase de estudiante 
# student1=Person("Juan","Torres",25)
student1=Person("Juan","Torres",25,"mates")
print(student1.showInfo())
profesional1=profesional("Ana","Fernando","30,","Enfermera")
print(profesional1.showInfor())

futbolist1=Futbolist("Lionel","Messi",38,"Inter Miami")
print(futbolist1)



