def obtener_min_max(numero):
    # Convertimos el número a cadena para recorrer sus dígitos
    digitos = str(numero)
    
    # Inicializamos min y max con el primer dígito
    minimo = int(digitos[0])
    maximo = int(digitos[0])
    
    # Recorremos los demás dígitos
    for d in digitos:
        d = int(d)
        if d < minimo:
            minimo = d
        if d > maximo:
            maximo = d
    
    return minimo, maximo


# Programa principal
num = int(input("Introduzca un número: "))

minimo, maximo = obtener_min_max(num)

print(f"El dígito menor de {num} es {minimo}")
print(f"El dígito mayor de {num} es {maximo}")