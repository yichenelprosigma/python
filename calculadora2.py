#una función con 3 argumentos

def calculate(numero1,numero2,operador):
    if operador=="+":
        suma=numero1+numero2
        print(suma)
    elif operador=="-":
        resta=numero1-numero2
        print(resta)
    elif operador=="*":
        multiplicacion=numero1*numero2
        print(multiplicacion)
    elif operador=="/":
        dividir=numero1/numero2
        print(dividir)
    else:
        print("no se puede, intentalo de nuevo")


calculate(10,5,"-")
calculate(22,10,"+")
calculate(5,2,"!")