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

matriz01=[[2,3,5],
         [7,2,4],]

matriz02=[[1,6],
         [7,2],
         [0,-5]]
# matrix diccionario
matrixArray={}

def main():
    matrixArray["matrixA"]=matriz01
    matrixArray["matrixB"]=matriz02
    print(matrixArray)
    while True:
        print("\n--- Bienvenido al sistema de gestión del edificio ---")
        print("1. Mostrar Matriz/Matrices")
        print("2. Mostrar una matriz seleccionada")
        print("3. Agregar una nueva matriz")
        print("4. Eliminar una matriz")
        print("5. Mostrar la traspuesta de una matriz")
        print("6. Eliminar persona de una planta")
        print("7. Cambiar la comisión de comunidad de una planta")
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
                print("Eliminar una matriz seleccionada")
               
            case 5:
                #Mostrar solo los nombres
                for name in matrixArray:
                    print(name)
                #preguntar al usuario la matriz traspuesta
                matriz_traspuesta=input("Elige la matriz que quieres mostrar la trapuestas ")
                showTranspose(matriz_traspuesta)
               
            # case 6:
             
            case 0:
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
