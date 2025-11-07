original ={
    "nombre":"Lilia",
    "edad": 25,
    "Ciudad":"Tenerife",
}
invers={}
for clave, valor in original.items():
    invers[valor]=clave

numeros=[2,3,4,2,3,2,5,3]
# numeros=[2,3,4,2,3,2,5,3]
#resultado:
#diccionario{
#   2:3,
#   3:3,
#   4:1,
#   5:1
#
#  }
frecuencia={}
for num in numeros:
    frecuencia[num]=frecuencia.get(num,0)+1
print(frecuencia)

for numero, veces in frecuencia.items():
    print(f"El número {numero} aparece {veces} veces")

#--------------------------------------------
alumnos = {
    "Juan": {"matematicas": 8, "ingles": 9, "historia": 7},
    "Maria": {"matematicas": 7, "ingles": 10, "historia": 9},
    "Carlos": {"matematicas": 6, "ingles": 8, "historia": 6},
    "Ana": {"matematicas": 9, "ingles": 9, "historia": 10},
    "Lucia": {"matematicas": 5, "ingles": 6, "historia": 7},
    "Pedro": {"matematicas": 8, "ingles": 7, "historia": 8},
    "Sofia": {"matematicas": 10, "ingles": 10, "historia": 9},
    "Miguel": {"matematicas": 7, "ingles": 6, "historia": 7},
    "Laura": {"matematicas": 8, "ingles": 9, "historia": 10},
    "David": {"matematicas": 6, "ingles": 8, "historia": 7}
}
alumnos_promedio = {}
for alumno, notas in alumnos.items():
    promedio = sum(notas.values()) / len(notas)
    print(f"El promedio de {alumno} es {promedio:.2f}")
    alumnos_promedio[alumno] = promedio
