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
