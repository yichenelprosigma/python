def cm_a_pulgadas(cm):
    return cm / 100

longitud = float(input("Introduzca longitud: "))
resultado = cm_a_pulgadas(longitud)
#imprimir la longitud que es 
print(f"{longitud} cm = {resultado:.2f} m")
