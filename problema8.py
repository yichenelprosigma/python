#guardar los números en una lista, finalmente imprimir la lista 
def potencias(n):
    lista=[]
    for i in range(n + 1):
        lista.append(2 ** i)
    print(lista)
potencias(10)
