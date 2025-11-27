#Ejercicio imprimir el resultado de 1-100 utilizando while
print("-----ejercicio 1-----")
i=1
suma=0
while i<=100:
    #realizar la suma de valores
    suma+=i
    #incrementado el valor para salir de while
    i +=1
    
print(suma)

print("-----ejercicio 2-----")



#Ejercicio 2: Comprobar una contraseña indicada
password_correct="123456"
password=""
while password != password_correct:
    password=input("Introduce la contraseña: ")
    if password != password_correct:
        print("Contraseña incorrecta, vuelve a intentarlo")

print("acceso correcta")