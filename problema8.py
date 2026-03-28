#guardar los números en una lista, finalmente imprimir la lista 
# def potencias(n):
#     lista=[]
#     for i in range(n + 1):
#         lista.append(2 ** i)
#     print(lista)
# potencias_usuario=int(input("Introduce un número"))
# potencias(potencias_usuario)

#modificación 
def potencias(base,veces):
    lista=[]
    for i in range(veces):
        lista.append(base*2**i)
    print(lista)
potencias_usuario=int(input("Introduce un número "))
potencias_veces=int(input("Introduce las veces "))
potencias(potencias_usuario,potencias_veces)
