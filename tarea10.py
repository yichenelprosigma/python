A=[[1,2],[3,4][5,6]]
#Filas: 0–2
#Columnas: 0–1

A[2][2]  #No existe, porque la columna 2 no existe.

A[1][0] #corresponde al número 3

N = int(input("Ingresa el número de filas (N): "))
M = int(input("Ingresa el número de columnas (M): "))

# Crear la matriz de NxM con valores 0
matriz = [[0 for _ in range(M)] for _ in range(N)]

# Imprimir la matriz
print("Matriz generada:")
for fila in matriz:
    print(fila)