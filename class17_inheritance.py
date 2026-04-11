# Tema: Herencia
# Concepto:


# Class padre= Animal
# Clases hijos= Perro, Gato, León, Panda, Oveja...

# Paso 1: Definir una clase padre
class Animal:
    def speak(self):
        print("Animal make sounds")

#Paso 2: Crear una clase hijo
class Dog():
    pass

# Crear 3: un objeto de la clase perro
dog1= Dog()
dog1.speak()