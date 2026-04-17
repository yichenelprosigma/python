def suma_multiplos(limite):
    suma = 0
    contador=0
    contador2=0
    for i in range(1, limite):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
            contador2 +=1
    
        else:
            contador += 1
    print(contador2)
    print(contador)
    return suma
resultado = suma_multiplos(1000)

print("La suma es:", resultado)