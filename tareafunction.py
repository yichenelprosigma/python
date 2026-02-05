def cm_a_pulgadas(cm):
    return cm / 2.54

longitud = float(input("Introduzca longitud: "))
resultado = cm_a_pulgadas(longitud)
print(f"{longitud} cm = {resultado:.2f} in")
