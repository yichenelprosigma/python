matrizb=[[1,6],
         [7,2],
         [0,-5],]
matriza=[[2,3,5],
         [7,2,4],]
matriz= [
     [1,2],
     [2,1],]
filas=len(matriz)
columnas=len(matriz[0])
matriz7=[[0 for j in range(filas)] for i in range(columnas)]
#2 Mostrar las matrices traspuestas
for i in range(filas):
    for j in range(columnas):
       matriz7[j][i]=matriz[i][j]
for fila in matriz7:
    print(fila)
#3 suma de las matrices
opcion = int(input("Elige una opción (1 o 2): "))
if opcion ==1:
    suma=0
    for fila in range(len(matrizb)):
        for columnas in range(len(matrizb[0])):
            suma+=matrizb[fila][columnas]
print("la suma de las fila", fila," es igual a", suma)
if opcion ==2:
    suma=0
    for fila in range(len(matriza)):
        for columnas in range(len(matriza[0])):
            suma+=matriza[fila][columnas]
print("la suma de las fila", fila," es igual a", suma)
#multiplicación 
if (len(matriza[0]) == len(matrizb)):
    print("Se pueden multiplicar las matrices")
    # paso2:código de crear una matriz final
    matrizc= [[0 for _ in range(len(matriza))] for _ in range(len(matrizb[0]))]
    print(len(matriza))
    print(len(matrizb[0]))

else:
    print("No se pueden multiplicar las matrices")
for i in range(len(matriza)): #recorrer filas de la matriz A
    for j in range(len(matrizb[0])): #filas de la matriz B y columna de de la matriz de A
        # matrizc[i][j]=0
        for k in range(len(matrizb)): #columnas de la matriz B
            matrizc[i][j] += matriza[i][k] * matrizb[k][j]
        print(matrizc)

