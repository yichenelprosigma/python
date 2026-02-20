# def calcular_hora_futura(hora_actual, horas_sumar):
#     return (hora_actual + horas_sumar) % 24


# hora_actual = int(input("Hora actual: "))
# horas_sumar = int(input("Cantidad de horas: "))

# resultado = calcular_hora_futura(hora_actual, horas_sumar)

# print(f"En {horas_sumar} horas, el reloj marcará las {resultado}")

#Modificación
def calcular_hora_futura(hora_actual, horas_sumar):
    return (hora_actual + horas_sumar) % 24


hora_actual = int(input("Hora actual: "))
horas_sumar = int(input("Cantidad de horas: "))

resultado = calcular_hora_futura(hora_actual, horas_sumar)
minutos= resultado*60
segundos=resultado*3600
print(f"En {horas_sumar} horas, el reloj marcará las {resultado} en minutos sería {minutos} y en sería {segundos}")