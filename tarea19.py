# Solicitar el radio al usuario
radio = float(input("Introduzca el radio: "))

# Definir el valor de pi
pi = 3.14

# Calcular perímetro y área
perimetro = 2 * pi * radio
area = pi * radio ** 2

# Mostrar resultados redondeados a 1 decimal
print("Perímetro:", round(perimetro, 1))
print("Área:", round(area, 1))