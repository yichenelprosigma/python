def obtener_min_max(numero):
    # Convertimos el número a cadena para recorrer sus dígitos
    digitos = str(numero)
    
    # Inicializamos min y max con el primer dígito
    minimo = int(digitos[0])
    maximo = int(digitos[0])
    suma=0
    
    # Recorremos los demás dígitos
    for d in digitos:
        d = int(d)
        suma+=d
        if d < minimo:
            minimo = d
        if d > maximo:
            maximo = d
    
    return minimo, maximo, suma
    

# Programa principal
num = int(input("Introduzca un número: "))

minimo, maximo, suma = obtener_min_max(num)

print(f"El dígito menor de {num} es {minimo}")
print(f"El dígito mayor de {num} es {maximo}")
print(f"El número total de {num} es {suma}")