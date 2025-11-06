# Qué es un diccionario en Python?
#(nombre: valor) #nombre es el clave y valor es el valor asociado a esa clave
#un diccionario es una estructura de datos que almacena pares clave-valor

#¿Cómo se crea un diccionario en Python?
#se crea usando llaves {}

#ejemplo:

empleados={
    "nombre":"Ana",
    "edad":25,
    "ciudad":"Tenerife",
}

print(empleados)

## imprimir algún valor concreto del diccionario
print(empleados["nombre"])  #imprime Ana
print(empleados["edad"])    #imprime 25
print(empleados["ciudad"])  #imprime Tenerife
# print(empleados["residencia"])  #genera error porque no existe esa clave

#imprimir otra formas
print(empleados.get("nombre"))  #imprime Ana
print(empleados.get("edad"))    #imprime 25
print(empleados.get("ciudad"))  #imprime Tenerife
print(empleados.get("residencia"))  #imprime None porque no existe esa clave, es más seguro.

#modificación del diccionario

empleados={
    "nombre":"Ana",
    "edad":25,
    "ciudad":"Tenerife",
}
#agregar una nueva clave-valor
empleados["genero"]="Femenino"
print(empleados)
#actualizar un valor existente
empleados["ciudad"]="lanzarote"
print(empleados)

#eliminar un clave-valor
#Usar del
del empleados["ciudad"]
print(empleados)
#2. usar pop
empleados["ciudad"]="lanzarote" #alt + teclado bajo
empleados.pop("ciudad")

#iteración sobre un diccionario
empleados={
    "nombre":"Ana",
    "edad":25,
    "ciudad":"Tenerife",
    "genero":"Femenino",
    "trabajo":"Ingeniera",
}
#iterar utilizando el bucle for
for clave in empleados:
    print(f"{clave}: {empleados[clave]}")#empleado[nombre]#empleado [edad]# empleado[ciudad], empleado[genero], empleado[trabajo]

for valor in empleados.values():
    print(valor)
#métodos de un diccionario
#ctrl +f2 después lo que tu quieras hacer
# ctrl+z #deshacer 
empleados={
    "nombre":"Ana",
    "edad":25,
    "ciudad":"Tenerife",
    "genero":"Femenino",
    "trabajo":"Ingeniera",
}
# dict.keys()	Devuelve todas las claves
empleados_keys=empleados.keys()
print(empleados_keys)

# dict.values()	Devuelve todos los valores
empleados_values=empleados.values()
print(empleados_values)


# dict.items()	Devuelve pares clave-valor
empleados_items=empleados.items()
print(empleados_items)
print(empleados)


# dict.get(clave, default)	Obtiene valor o default


# dict.pop(clave)	Elimina clave y devuelve valor


# dict.popitem()	Elimina último par clave-valor
empleados_popitem=empleados.popitem()
print(empleados_popitem)

# dict.update(otro_dict) Añade o actualiza claves con otro diccionario

# dict.clear()	Elimina todos los elementos
empleados_clear= empleados.clear()
print(empleados_clear)

# direccionario añadidos
#alt+ shift + flecha abajo/arriba
# #duplicar línea

# #alumnos={
#     "nombre":"Ana",
#     "edad":"16",
#     "notas":{
#         "matematicas":9,
#         "lengua":10,
#         "ingles":8,
#     },

# }
# print(alumnos["notas"]["matematicas"])  #imprime 9
#imprimir con varios alumnos 
#Fallo: la clave no se puede repetir, porque en este caso, estoy poniendo nombre muchas veces, tengo que separarlo
alumnos={
    "nombre":"Ana",
    "edad": 16,
    "notas":{
        "matematicas":9,
        "lengua":10,
        "ingles":8,
    },

    "nombre":"Maria",
    "edad": 17,
    "notas": {
        "matematicas":7,
        "lengua":9,
        "ingles":10,
    },

    "nombre":"Luisa",
    "edad": 16,
    "notas": {
        "matematicas":8,
        "lengua":7,
        "ingles":9,
    },

}

for alumno in alumnos:
    print(alumno["nombre"])
    print(alumno["edad"])
    #imprimir todas los datos a la vez o uno a uno
    print(alumno["notas"])
     #imprimir paso a paso
    for nota in alumno["notas"]:
         print(notas["matematicas"])
         print(notas["lengua"])
         print(notas["ingles"])
        
       
    