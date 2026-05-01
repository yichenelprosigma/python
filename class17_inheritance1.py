# # # Tema: Herencia
# # # Concepto: En la POO(programación orientada a objetos), es compartir atributos (variables) y métodos (funciones) entre clases

# # # crear una instancia o objeto

# # # Class padre= Animal
# # # Clases hijos= Perro, Gato, León, Panda, Oveja...

# # # Paso 1: Definir una clase padre
# # class Animal:
# #     def speak(self):
# #         print("Animal make sounds")

# # #Paso 2: Crear una clase hijo
# # class Dog():
# #     pass

# # # Crear 3: un objeto de la clase perro
# # dog1= Dog()
# # dog1.speak()

# # class Student:
# #     #constructor de la clase cuando se crea el hace todo
# #     def __init__(self):
# #         self.name=name
        
# # estudiante1= Student("Juan")
# # print(estudiante1.name)

# # Constructor por defecto y constructor definido

# #Ejemplo de override
# # ejemplo de clase heredada:
# class Person:
#     def __init__(self,name, lastname, age):
#         self.name=name
#         self.lastname=lastname
#         self.age=age
#     def showInfo(self):
#         txt= "full name= {0} {1}, age= {2}"
#         return txt.format(self.name, self.lastname, self.age)


# class Student(Person):
#     def __init__(self, name, lastname, age, degree):
#         #se refiere la clase padre 
#         super().__init__(name, lastname, age)
#         self.degree = degree
    
#     # override of the function showInfo 
#     def showinfo(self):
#         print(f"Información del estudiante:{self.name}, {self.lastname}, tiene {self.age}, está estudiando en {self.degree} ")
    
# class profesional(Person):
#     def __init__(self, name, lastname, age, profesion):
#         super().__init__(name, lastname, age)
#         self.profesion= profesion
# class deportista(Person):
#     def __init__(self, name, lastname, age, deporte):
#         super().__init__(name, lastname, age)
#         self.deporte=deporte
# class Futbolist(deportista):
#     def __init__(self, name,lastname, age, team):
#         super().__init__(name,lastname, age, "futbol")
#         self.team=team


# multiples herencias 
# una clase puede tener una o más clases padres 
# class A:
#     def helloworld(self):
#         print("Helloworld from the class A")
# class B:
#     def helloworld(self):
#         print("Helloworld from the class B")

# class Hija(A,B):
#     #override 
#     def helloworld(self):
#         print("Helloworld from the class C")

# obj1=Hija()
# obj1.helloworld()

# Ejemplo concreto
#tenemos un robot en la casa, robot puede cocina(cocinero), puede limpiar(limpiador), puede...

# cocinero 
class Chef:
    def cook(self):
        input("Qué comida quieres comer")
        print("voy a preparar, esperame un minuto")

class Cleaner:
    def clean(self):
        print("I am going to clean the house")

class HomeRobot(Chef,Cleaner):
    def hello(self):
        print("Hello,I am your HomeRobot")

def main():
    robot = HomeRobot()
    robot.hello()
    while True:
        print("\n--- Bienvenido al sistema de HomeRobot ---")
        print("1. Cook somethings")
        print("2. Clean the house")
        print("0. Salir")
        option = int(input("\nChoose an opcion: "))
        print(option)
        match option:
            case 1:
                robot.cook()
            case 2:
                robot.clean()
            case 0: 
                print("Exit")
                break
            case _:
                print("\n variación invariable")

                
if __name__ == "__main__":
    main()