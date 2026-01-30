# matrizb=[[1,6],
#          [7,2],
#          [0,-5],]
# matriz01=[[2,3,5],
#          [7,2,4],]

#para imprimir más matrices añadidas
#Imprimir todas las matrices
def showAllMatrix():
    for name, matrix in matrixArray.items():
        print(name)
        print(matrix)
        
#Imprimir una matriz seleccionada
def showAMatrix(name):
    #comprobar si está a dentro del diccionario
    if name not in matrixArray: 
        print("La matriz no existe")
        return
    #encontrar la matriz en el diccionario
    matrix=matrixArray[name]
    #imprimir la matriz
    for i in range(len(matrix)):
        print("[",end="")
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=",")
        print("]")


#Agregar una nueva matriz
def createMatrix(fila,columna):
    print("Crear una matrix nueva")
    # crear una matriz vacia con 0
    matriz=[[0 for _ in range(columna)]for _ in range(fila)]
    #recorrer cada posición para sustituir
    for i in range(fila):
        for j in range(columna):
            valor = int(input(f"Valor en la posición [{i}][{j}]: "))
            matriz[i][j]= valor
    
    # hacer más bonito
    print(matriz)
    name="matrix"+str(len(matrixArray)+1)
    print(name)
    matrixArray[name]= matriz
def renameMatrices():
    # crear un nuevo diccionario
    matrices={}
    #empieza con  la matriz 1
    contador = 1
    #recorrer el diccionario
    for _ , matrix in matrixArray.items():
        newName= "matrix"+ contador
        matrices[newName]= matrix
        contador +=1
    matrixArray.clear()
    matrixArray.update(matrices)
def deleteMatrix(name):
    if name not in matrixArray:
        print("La matriz no existe")
        return
    del matrixArray[name]
    print("Matriz Eliminada")
    #renombrar todas las matrices
    renameMatrices()
    print("Renombramos todas las matrices")
def showTranspose(name):
    if name not in matrixArray: 
        print("La matriz no existe")
        return
    matrix= matrixArray[name]
    #mostrar la traspuesta
    #obtener N de filas y M de columnas
    filas=len(matrix)
    columnas=(len(matrix[0]))
    #Crear un matriz vacia de M filas y N de columnas
    matrizT=[[0 for _ in range(filas)] for _ in range(columnas)]
    # Voy a recorrer mi matrixT, cambiar sus filas
    for i in range(filas):
        for j in range(columnas):
            matrizT[j][i]=matrix[i][j]
    #impirmir el MatrixT
    for fila in matrizT:
        print(fila)
# ctrl+f=para buscar una palabra
def sumofmatrix(matrixA,MatrixB):
    #comprobar que dos matrices están en el diccionario
    if matrixA not in matrixArray or MatrixB not in matrixArray:
        print("Unas de las matrices seleccionados no existen")
        return
    matriz1= matrixArray[matrixA]
    matriz2= matrixArray[MatrixB]
    #comprobar las dimensiones sean iguales
    if len (matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("No se pueden realizar la suma, puesto que las dimensiones son distintas")
        return
    #crear una matrix vacía para guardar el resultado de la suma
    suma_de_las_matrices=[[0 for _ in range(len(matriz1[0]))] for _ in range(len(matriz1))]

    for i in range(len(matriz1)):
        for j in range (len(matriz1[0])):
            suma_de_las_matrices[i][j]=matriz1[i][j]+ matriz2[i][j]
    print("Imprimir la suma:")
    for i in range(len(suma_de_las_matrices)):
        print("[", end=" ")
        for j in range(len(suma_de_las_matrices[0])):
            print(suma_de_las_matrices[i][j], end= ", ")
        print("]")
def multiplyofmatrix(name1,name2):
    if name1 not in matrixArray or name2 not in matrixArray:
        print("No se pueden realizar la suma, puesto que las dimensiones son distintas")
        return
    matrix1= matrixArray[name1]
    matrix2= matrixArray[name2]
    #comando para replicar la linea entera alt+ shift + arriba/ abajo
    if (len(matrix1[0])!= len(matrix2)):
        print("no se puede realizar la multiplicación, puesto que N de fila de matrizA no coincide con la N columna de matrixB. ")
    #la matriz vacía para el resultado de la multiplicación
    #columnas de B y filas A
    multiplicación_matriz=[[0 for _ in range(len(matrix1))]for _ in range(len(matrix2[0]))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                multiplicación_matriz[i][j]+= matrix1[i][k] * matrix2[k][j]
    
    for i in range(len(multiplicación_matriz)):
        print("[", end=" ")
        for j in range(len(multiplicación_matriz[0])):
            print(multiplicación_matriz[i][j], end= ", ")
        print("]")


def sumofmatrix(matrixA,MatrixB):
     if matrixA not in matrixArray or MatrixB not in matrixArray:
        print("Unas de las matrices seleccionados no existen")
        return
     matrix1=matrixArray[matrixA]
     matrix2=matrixArray[MatrixB]


def sumTaskMatrices(matrixA,matrixB):
    # comprobar que existen
    if matrixA not in matrixArray or matrixB not in matrixArray:
        print("Las matrices no existen")
        return

    matriz1 = matrixArray[matrixA]
    matriz2 = matrixArray[matrixB]

    # comprobar dimensiones
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("No se pueden sumar, dimensiones distintas")
        return

    # crear matriz vacía
    suma = [[0 for _ in range(len(matriz1[0]))] for _ in range(len(matriz1))]

    # sumar
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            suma[i][j] = matriz1[i][j] + matriz2[i][j]

    print("Imprimir la suma (matrix4 + matrix5):")

    for i in range(len(suma)):
        print("[", end=" ")
        for j in range(len(suma[0])):
            print(suma[i][j], end=", ")
        print("]")

matriz01=[[2,3,5],
         [7,2,4],]
matriz02=[[1,6],
         [7,2],
         [0,-5]]
matriz03=[[1,1,1],
         [2,2,2],]
matrix04 = [
     [2, 3, 5],
     [7, 2, 4],
 ]

matrix05 = [
    [1, 6],
    [7, 2],
    [0, -5] ]
matrixArray={}

def main():
    matrixArray["matrix1"]=matriz01
    matrixArray["matrix2"]=matriz02
    matrixArray["matrix3"]= matriz03
    matrixArray["matrix4"]=matrix04
    matrixArray["matrix5"]=matrix05
    print(matrixArray)
    while True:
        print("\n--- Bienvenido al sistema de gestión del edificio ---")
        print("1. Mostrar Matriz/Matrices")
        print("2. Mostrar una matriz seleccionada")
        print("3. Agregar una nueva matriz")
        print("4. Eliminar una matriz")
        print("5. Mostrar la traspuesta de una matriz")
        print("6. Mostrar la suma de dos matrices")
        print("7. Mostrar la multiplicación de dos matrices")
        print("8. Suma automática (matrix4 + matrix5)")
        print("0. Salir")
        
        option = int(input("\nSeleccione una opción: "))

        print(option)
        match option:
            case 1:
                print("Imprimiendo todas las matrices...")
                showAllMatrix()
            case 2:
                #mostrar todos los nombres de la matrices
                for name in matrixArray:
                    print(name)
                matrix=input("elige la matriz que quieres imprimir ")
                showAMatrix(matrix)  
            case 3:
                fila= int(input("Introduzca el número de las filas: "))
                columna= int(input("introduzca el número de la columna:  "))
                createMatrix(fila, columna)    
            case 4:
                for name in matrixArray:
                    print(name)
                print("Eliminar una matriz seleccionada")
                matriz_elimninar=input("elige la matriz que quieres eliminar ")
                deleteMatrix(matrix)               
            case 5:
                #Mostrar solo los nombres
                for name in matrixArray:
                    print(name)
                #preguntar al usuario la matriz traspuesta
                matriz_traspuesta=input("Elige la matriz que quieres mostrar la trapuestas ")
                showTranspose(matriz_traspuesta)
               
            case 6:
                showAllMatrix()
                matrixA=input("Elige la matriz A para sumar ")
                matrixB=input("Elige la matriz B para sumar ")
                sumofmatrix(matrixA,matrixB)
            case 7:
                showAllMatrix()
                # ¡elegir matrices con sui nombre solo !
                matrixA= input("Elige la matriz A para multiplicar")
                matrixB= input("Elige la matriz B para multiplicar")
                multiplyofmatrix(matrixA,matrixB)
            case 8:

                print("Sumando matrices nuevas matrix04 + matrix05")

                matrixA = "matrix4"
                matrixB = "matrix5"

                sumTaskMatrices(matrixA,matrixB)

            case 0:
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()

#tarea 
# matrix1 = [
#     [2, 3, 5],
#     [7, 2, 4]
# ]

# matrix2 = [
#     [1, 6],
#     [7, 2],
#     [0, -5]
# ]