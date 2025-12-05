#Matriz con datos introducidos por el usuario
# Matriz=[[6,4,5],[9,10,7]]

n=int(input("Ingrese el número de filas de la matriz: "))
m=int(input("Ingrese el número de columnas de la matriz: "))

print("Es una matriz de",n,"x",m)

matriz=[]
for i in range(n):
    fila=[]
    for j in range(m):
        valor=int(input(f"valor [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

print(matriz)

#imprimir el valor en la posicion [1][1]
Matriz=[[6,4,5],[9,10,7]]
print(Matriz[1][1])
#imprimir una fila completa, por ejemplo la fila 0
print(Matriz[0])
#imprimir una columna completa, por ejemplo la columna 0
columna = [Matriz[i][0] for i in range(len(Matriz))]
print(columna)

#Ejemplo de 2:
Matriz2=[[6,4,5],[9,7,9],[1,2,3]]
#Recorrer una matriz con sus índices:
print("recorrer una matriz con sus índices usando for")
for i in range(len(Matriz2)):#fila 0 - fila 1 - fila 2
    for j in range(len(Matriz2[i])):# recorrer la posición 0,1,2...
        print(Matriz2[i][j])
print("recorrer una matriz con los valores usando for each para valores")
for fila in Matriz2:
    for valor in fila:
        print(valor)
        