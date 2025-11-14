edificio = {
    "planta1": {
        "numero_personas": 2,
        "personas": [
            {"nombre": "Ana", "edad": 25, "genero": "mujer"},
            {"nombre": "Luis", "edad": 30, "genero": "hombre"}
        ],
        "comision_comunidad": 50.0
    },
    "planta2": {
        "numero_personas": 3,
        "personas": [
            {"nombre": "Carlos", "edad": 40, "genero": "hombre"},
            {"nombre": "Lucía", "edad": 35, "genero": "mujer"},
            {"nombre": "Pepe", "edad": 20, "genero": "hombre"}
        ],
        "comision_comunidad": 70.0
    }
}

def mostrar_informacion(edificio):
    for planta, datos in edificio.items():
        print(f"\n{planta.upper()}:")
        print(f"  Número de personas: {datos['numero_personas']}")
        print(f"  Comisión comunidad: {datos['comision_comunidad']}")
        print("  Personas:")
        for p in datos["personas"]:
            print(f"    - {p['nombre']}, {p['edad']} años, {p['genero']}")

def agregar_planta(edificio, nombre_planta, numero_personas, personas, comision):
    edificio[nombre_planta] = {
        "numero_personas": numero_personas,
        "personas": personas,
        "comision_comunidad": comision
    }

def total_comision(edificio):
    total = sum(p["comision_comunidad"] for p in edificio.values())
    return total

def mayores_30(edificio):
    mayores = []
    for planta in edificio.values():
        for persona in planta["personas"]:
            if persona["edad"] > 30:
                mayores.append(persona)
    return mayores

def agregar_persona(edificio, planta, persona):
    edificio[planta]["personas"].append(persona)
    edificio[planta]["numero_personas"] += 1

def eliminar_persona(edificio, planta, nombre):
    personas = edificio[planta]["personas"]
    edificio[planta]["personas"] = [p for p in personas if p["nombre"] != nombre]
    edificio[planta]["numero_personas"] = len(edificio[planta]["personas"])
    
def cambiar_comision(edificio, planta, nueva_comision):
    edificio[planta]["comision_comunidad"] = nueva_comision
#hacer un switch para ejecutar las tareas
# ------------------------------Bienvenido al sistema gestion del edificio------------------------------    
#Elija la opción que desea realizar:
#1. Mostrar información del edificio
#2. Agregar planta
#3. Agregar persona a una planta
#4. calcular total comisión de la comunidad
#5. eliminar persona de una planta
# 6. Cambiar la comisión de comunidad de una planta



#activar funciones

def main():
    mostrar_informacion(edificio)

    agregar_planta(
        edificio,
        "planta3",
        2, [{"nombre": "Marta", "edad": 50, "genero": "mujer"},{"nombre": "Andrés", "edad": 55, "genero": "hombre"}],
        60.0)
    # 2 vez que muestra la información
    mostrar_informacion(edificio)

    #3. Total comision
    total = total_comision(edificio)
    print(f"\nTotal comisión de la comunidad: {total}")
    #4. Mayores de 30
    #personas_mayores es una lista
    personas_mayores = mayores_30(edificio)
    for persona in personas_mayores:
        print(f"\nPersona mayor de 30: {persona['nombre']}, {persona['edad']} años, {persona['genero']}")
    #5. Agregar persona
    agregar_persona(edificio, "planta3", {"nombre": "Sofía", "edad": 28, "genero": "mujer"})
    #6.mostrar info
    mostrar_informacion(edificio)
    #7. Eliminar persona
    eliminar_persona(edificio,"planta1",{"nombre": "Ana"})
    mostrar_informacion(edificio)
    #8. Cambiar comision
    cambiar_comision(edificio,"planta3",80.0)
    mostrar_informacion(edificio)
# personas = [
#     {"nombre": "Marta", "edad": 50, "genero": "mujer"},
#     {"nombre": "Andrés", "edad": 55, "genero": "hombre" comision_comunidad = 60.0

#  "planta3": {
#      "numero_personas": 2,
#      "personas": [
#          {"nombre": "Marta", "edad": 50, "genero": "mujer"},
#          {"nombre": "Andrés", "edad": 55, "genero": "hombre"}
#      ],
#      "comision_comunidad": 60.0
# }


if __name__ == "__main__":
    main()
