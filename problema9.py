
def invertir_con_lista():    
    # Convertir a lista, invertir la lista y unirla de nuevo
    lista_digitos = list(numero)
    lista_digitos.reverse()
    lista_int= list(map(int,lista_digitos))
    print(lista_int)
    # for i in lista_digitos:
    #     print(i,end="")
    # # for i, num in enumerate(lista_digitos) solo el valor y posición
    #     print(f"")
    resultado=0
    for pos in range (len(lista_int)):
        # print(pos)
        if pos % 2==0:
            resultado+=lista_int[pos]
            print(resultado,end="")

        else:
            resultado-=lista_int[pos]
            print(resultado,end="")

numero = input("Introduzca un número: ")
invertir_con_lista()