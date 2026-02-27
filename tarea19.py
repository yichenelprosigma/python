# # Solicitar el radio al usuario
# radio = float(input("Introduzca el radio: "))

# # Definir el valor de pi
# pi = 3.14

# # Calcular perímetro y área
# perimetro = 2 * pi * radio
# area = pi * radio ** 2

# # Mostrar resultados redondeados a 1 decimal
# print("Perímetro:", round(perimetro, 1))
# print("Área:", round(area, 1))

# #modificado
# radio = float(input("Introduzca el radio: "))
# pi=3.14
# def calcular_area(radio):
#     perimetro= 2* pi*radio
#     area= pi* radio **2
#     print("Perímetro:", round(perimetro, 2))
#     print("Área:", round(area, 2))
# calcular_area(radio)

def calcular_triangulo (Base,altura):
    area=Base*altura/2
    print("El área de este triángulo es", area)
def calcular_rectangulo (Base,altura):
    area=Base*altura
    print("El área de este rectangulo es", area)
def calcular_circulo (radio,pi):
    area= pi * radio **2
    print("El área de este círculo es", area)
def calcular_cuadrado (lado):
    area=lado**2
    print("El área de este cuadrado es", area)



def main():
    while True:
        print("\n--- Bienvenido al sistema de gestión del geometría ---")
        print("1. Calcular un triángulo")
        print("2. Calcular un rectangulo")
        print("3. Calcular un círculo")
        print("4. Calcular un cuadrado")
        print("0. Salir")
        option = int(input("\nSeleccione una opción: "))
        print(option)
        match option:
            case 1:
                base=float(input("Cuánto mide la base "))
                altura=float(input("Cuánto mide la altura "))
                calcular_triangulo(base,altura)
            case 2:
                base=float(input("Cuánto mide la base "))
                altura=float(input("Cuánto mide la altura "))
                calcular_rectangulo(base,altura)
            case 3:
                radio=float(input(" Cuánto mide el radio "))
                pi=3.14
                calcular_circulo(radio,pi)
            case 4:
                lado=float(input("Cuanto mide el lado "))
                calcular_cuadrado(lado)
            case 0: 
                print("Saliendo el sistema...")
                break
                
if __name__ == "__main__":
    main()