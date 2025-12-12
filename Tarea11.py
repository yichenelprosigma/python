# #Aquí está mi explicación y el código solicitado.
# # Pedir una matriz 3x3 columna por columna y mostrarla progresivamente


# matriz = [[0, 0, 0] for _ in range(3)]  # Inicializamos matriz 3x3 con ceros

# # Recorremos columna por columna
# for columnas in range(3):
    
#     print(f"Ingrese los valores de la columna {columnas+1}:")
#     for fila in range(3):
#         valor = int(input(f"Fila {fila+1}: "))
#         matriz[fila][columnas] = valor
    
#     # Mostrar la matriz parcialmente completada hasta la columna actual
#     print("Matriz actual:")
#     for fila in matriz:
#         # Mostrar solo hasta la columna actual + 1
#         print(fila[:columnas+1])
#     print()  # Línea en blanco para separar pasos

# # Al final imprimir la matriz completa
# print("Matriz final completa:")
# for fila in matriz:
#     print(fila)
#Aquí está mi explicación y el código solicitado.
# Pedir una matriz 3x3 columna por columna y mostrarla progresivamente

                                                            #Modificación del ejercicio 1#
matriz = [[0, 0, 0] for _ in range(3)]  # Inicializamos matriz 3x3 con ceros

# Recorremos columna por columna
for columnas in range(3):
    print(f"Ingrese los valores de la columna {columnas+1}:")
    for fila in range(3):
        if columnas==fila:
            matriz[fila][columnas] = 2
    # Mostrar la matriz parcialmente completada hasta la columna actual
    print("Matriz actual:")
    for fila in matriz:
        # Mostrar solo hasta la columna actual + 1
        print(fila[:columnas+1])
    print()  # Línea en blanco para separar pasos

# Al final imprimir la matriz completa
print("Matriz final completa:")
for fila in matriz:
    print(fila)
# [2, 0, 0]
# [0, 2, 0]
# [0, 0, 2]