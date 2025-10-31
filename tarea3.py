from datetime import datetime
estudiantes=(
    ("Ana",(8,9,10)),
    ("Luis",(7,6,9)),
    ("Maria",(10,10,9))
)
print(estudiantes[0])

list_estudiantes=list(estudiantes)
for estudiante in list_estudiantes:
    nombre=estudiante[0]
    notas=estudiante[1]
    promedio=sum(notas)/len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")
#2 Encontrar esudiante con el promedio más alto en el tercercuatrimeste y mostrar su nombre y promedio

#segundo ejercicio
datos=("Madrid",2025,(28.3, -16.6))
ciudad, año, coordenadas=datos
# coordenadas_lat, coordenadas_long=coordenadas
#para obtener tuplas separadas.
print("la ciudad es:", ciudad, "el año es:", año, "las coordenadas son:", coordenadas)
#tarea 3
empleados=(
    ("Ana","15/03/1992","Mujer"),
    ("Luis","22/07/1985","Hombre"),
    ("Carmen","09/10/2001","Mujer"),
    ("Pablo","03/12/1990","Hombre"),
    ("Sofía","28/04/1998","Mujer"),
    ("Miguel","12/06/1980","Hombre"),
    ("Laura","19/11/1993","Mujer"),
    ("Javier","25/01/2002","Hombre"),
    ("Elena","07/09/1988","Mujer"),
    ("Diego","30/05/1995","Hombre")
)
today = datetime.now()
for empleado in empleados:
    nombre, fecha_nacimiento, genero=empleado
    day, month, year = map(int, fecha_nacimiento.split('/'))
    age = today.year - year
    if age>30:
        print(f"Empleado: {nombre}, Edad: {age}, Género: {genero}")