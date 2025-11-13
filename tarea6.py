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


