
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Este animal hace un sonido")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        print("Guau guau")

    def correr(self):
        print(f"{self.nombre} está corriendo")
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        print("Miau")

    def trepar(self):
        print(f"{self.nombre} está trepando")
class Ave(Animal):
    def __init__(self, nombre, edad, puede_volar):
        super().__init__(nombre, edad)
        self.puede_volar = puede_volar

    def hacer_sonido(self):
        print("Pío pío")

    def volar(self):
        if self.puede_volar:
            print(f"{self.nombre} está volando")
        else:
            print(f"{self.nombre} no puede volar")
perro = Perro("Firulais", 3, "Labrador")
gato = Gato("Michi", 2, "Blanco")
ave = Ave("Piolín", 1, True)

perro.hacer_sonido()
gato.hacer_sonido()
ave.hacer_sonido()

perro.correr()
gato.trepar()
ave.volar()