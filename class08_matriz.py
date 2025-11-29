#matriz 
# ¿Qué es una matriz exactamente?
# Matriz se forma con N filas y M columnas [ N y M son números enteros positivos ]
#Matriz es una lista de listas en Python

#ejemplos de matrices
matriz1=[1,2,3] # 1x3 1 fila y 3 columnas

matriz2=[[1,1],[2,2]]# 2x2 2 filas y 2 columnas

matriz3=[[1,2,3],[4,5,6]] # 2x3 2 filas y 3 columnas

#Crear matriz
#crear una matriz manualmente
matriz4=[[2,3],[4,5]] # matriz de 2x2
print(matriz4)

#crear una matriz vacía
matriz5=[]
print(matriz5)

#crear  una matriz con valor 0
filas=3
columnas=3
matriz6=[[0 for _ in range(columnas)] for _ in range(filas)]
#crear una fila con m columnas
#cada columna tiene el valor de 0
# _ significa que no nos importa el valor de la variable
print(matriz6)
