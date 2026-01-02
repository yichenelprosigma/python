#Tarea 1
matrix = [ [1, 2, 1, 1, 0],
[0, 1, 0, 0, 1],
[1, 0, 2, 0, 0],
[1, 2, 0, 1, 2],
[0, 2, 1, 0, 1] ]

contador=0
for i in range (len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]==0:
            contador+=1
print("cantidad de números 0 es", contador)

notas = [
[85, 92, 78, 88, 95], # alumno1
[67, 88, 95, 72, 81], # alumno2
[99, 79, 88, 93, 89], # alumno3
[45, 52, 61, 58, 49], # alumno4
[77, 82, 90, 50, 42], # alumno5
[95, 98, 91, 96, 93], # alumno6
[25, 33, 77, 24, 41], # alumno7
[72, 65, 78, 74, 69], # alumno8
[43, 90, 33, 60, 32], # alumno9
[59, 62, 55, 61, 58],] # alumno10
suma=0
Eso_01={
    "A":{},
    "B":{},
    "C":{},
    "D":{}

}
for fila in range (len(notas)):
    suma=0
    for columnas in range(len(notas[0])):
        suma=suma+notas[fila][columnas]  
    nota_media= suma/ len(notas[0])
    if nota_media>90:
        Eso_01["A"][fila]=nota_media
    if nota_media<90 and nota_media>70:
        Eso_01["B"][fila]=nota_media
    if nota_media<70 and nota_media>50:
        Eso_01["C"][fila]= nota_media
    else:
        Eso_01["D"][fila]= nota_media
print(Eso_01)
        


    
    
    
    
    
    
    
    
    # if [fila][columnas]>90:
    #     print("A")
    # if [fila][columnas]<90 and [fila][columnas]>70:
    #     print("B")
    # if [fila][columnas]<70 and [fila][columnas]>50:
    #     print("C")
    # else:
    #     print("D")