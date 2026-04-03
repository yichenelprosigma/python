
def invertir_con_lista():    
    # Convertir a lista, invertir la lista y unirla de nuevo
    lista_digitos = list(numero)
    lista_digitos.reverse()

    print(lista_digitos)
numero = input("Introduzca un número: ")
invertir_con_lista()