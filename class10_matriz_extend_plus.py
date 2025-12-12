# matriz=[[2,0,0],
#         [0,2,0],
#         [0,0,2]]

# matriz[0][0]=3
# matriz[1][1]=3
# matriz[2][2]=3
# print(matriz)
# # reemplazar fila entera

# matriz[0]=[1,2,3]
# print(matriz)
# #Insertar una nueva fila
# matriz.insert(1,[2,2,2])
# print(matriz)
# #Eliminar una fila
# matriz.pop(3)
# print(matriz)

#Matriz traspuesta
#Paso 1: Definir/obtener la matriz
matriz2=[
     [6,4,5],
     [9,10,7],
     [1,2,1],
]
#Paso2: obtener N de filas y N de columnas
filas=len(matriz2)
columnas=len(matriz2[0])

#Paso 3: Crear una matriz vacia de M filas y N columnas
#coger filas x columnas, convertir en el tamaño de columnas x filas
matriz7=[[0 for j in range(filas)] for i in range(columnas)]
#Paso 4: aquí lo que voy a hacer es correr la Matriz, cambiar sus filas en columnas
for i in range(filas):
    for j in range(columnas):
       matriz7[j][i]=matriz2[i][j]
#Imprimir mi matriz llamado matriz7
for fila in matriz7:
    print(fila)
