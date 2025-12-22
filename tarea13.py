# Tarea A

MatrizA = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
]

MatrizB = [
    [1, 2, 3],
    [4, 5, 6],
]

# Paso 1: Imprimir las dos matrices
# print("Matriz A:")
# for fila in MatrizA:
#     print(fila)

# print("\nMatriz B:")
# for fila in MatrizB:
#     print(fila)

# # Paso 2: Transpuesta de las matrices
# Matriz_TraspuestaA=[[0 for j in range(len(MatrizA[0]))] for i in range(len(MatrizA))]
# for i in range(len(MatrizA)):
#     for j in range(len(MatrizA[0])):
#        Matriz_TraspuestaA[j][i]=MatrizA[i][j]
# Matriz_TraspuestaB=[[0 for j in range(len(MatrizB[0]))] for i in range(len(MatrizB))]
# for i in range(len(MatrizB)):
#     for j in range(len(MatrizB[0])):
#        Matriz_TraspuestaB[j][i]=MatrizB[i][j]
# print("\nTranspuesta de la Matriz A:")
# for fila in Matriz_TraspuestaA:
#     print(list(fila))

# print("\nTranspuesta de la Matriz B:")
# for fila in Matriz_TraspuestaB:
#     print(list(fila))

if len(MatrizA)==len(MatrizB) and len(MatrizA[0])==len(MatrizB[0]):

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
else:
    print("no se puede hacer esta suma")
