def calcular_suma(a, b):
    resultado = a + b
    print("El resultado de la suma es", resultado)

def calcular_resta(a, b):
    resultado = a - b
    print("El resultado de la resta es", resultado)

def calcular_multiplicacion(a, b):
    resultado = a * b
    print("El resultado de la multiplicación es", resultado)

def calcular_division(a, b):
    if b != 0:
        resultado = a / b
        print("El resultado de la división es", resultado)
    else:
        print("Error: división por cero")


def main():
    while True:
        print("\n--- Bienvenido al sistema de la calculadora ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Salir")

        option = int(input("\nSeleccione una opción: "))

        match option:
            case 1:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                calcular_suma(a, b)

            case 2:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                calcular_resta(a, b)

            case 3:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                calcular_multiplicacion(a, b)

            case 4:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                calcular_division(a, b)

            case 0:
                print("Saliendo del sistema...")
                break


if __name__ == "__main__":
    main()