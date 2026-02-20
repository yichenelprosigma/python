#Programa para calcular la media de cuatro valores

# # Solicitar valores al usuario
# v1 = float(input("Primer valor: "))
# v2 = float(input("Segundo valor: "))
# v3 = float(input("Tercer valor: "))
# v4 = float(input("Cuarto valor: "))

# # Calcular la media
# media = (v1 + v2 + v3 + v4) / 4

# # print("La media es:", media)
# #ahora hacerla función
# v1 = float(input("Primer valor: "))
# v2 = float(input("Segundo valor: "))
# v3 = float(input("Tercer valor: "))
# v4 = float(input("Cuarto valor: "))

# def media(v1,v2,v3,v4):
#     return (v1+v2+v3+v4)/4
# resultado=media(v1,v2,v3,v4)

# print("la media es",resultado)

list1=[10,20,30,40]


def media(param1):
    suma=0
    for valor in param1:
        print(valor)
        suma+=valor
    resultado=suma/4
    print(resultado)
media(list1)
    

