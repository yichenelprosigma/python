# Tarea A

MatrizA = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
]

MatrizB = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Paso 1: Imprimir las dos matrices
print("Matriz A:")
for fila in MatrizA:
    print(fila)

print("\nMatriz B:")
for fila in MatrizB:
    print(fila)

# Paso 2: Transpuesta de las matrices
TranspuestaA = list(zip(*MatrizA))
TranspuestaB = list(zip(*MatrizB))

print("\nTranspuesta de la Matriz A:")
for fila in TranspuestaA:
    print(list(fila))

print("\nTranspuesta de la Matriz B:")
for fila in TranspuestaB:
    print(list(fila))

# Paso 3: Suma de las dos matrices
Suma = []
for i in range(len(MatrizA)):
    fila = []
    for j in range(len(MatrizA[0])):
        fila.append(MatrizA[i][j] + MatrizB[i][j])
    Suma.append(fila)

print("\nSuma de la Matriz A y Matriz B:")
for fila in Suma:
    print(fila)
