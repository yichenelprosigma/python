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
#hacer un switch para ejecutar las tareas
# ------------------------------Bienvenido al sistema gestion del edificio------------------------------    
#Elija la opción que desea realizar:
#1. Mostrar información del edificio
#2. Agregar planta
#3. Agregar persona a una planta
#4. calcular total comisión de la comunidad
#5. eliminar persona de una planta
# 6. Cambiar la comisión de comunidad de una planta
def mostrar_informacion():
    print("\n--- Información del edificio ---")
    for planta, datos in edificio.items():
        print(f"{planta}:")
        print(f"  Personas: {datos['numero_personas']}")
        print(f"  Comisión comunidad: {datos['comision_comunidad']}€")
        print("  Lista de personas:")
        for p in datos["personas"]:
            print(f"    - {p['nombre']} ({p['edad']} años, {p['genero']})")
    print("--------------------------------\n")


def agregar_planta():
    nueva = input("Nombre de la nueva planta (ej: planta3): ")
    if nueva in edificio:
        print("Esa planta ya existe.")
        return
    
    edificio[nueva] = {
        "numero_personas": 0,
        "personas": [],
        "comision_comunidad": 0.0
    }
    print(f"Planta '{nueva}' añadida correctamente.")


def agregar_persona():
    planta = input("Ingrese la planta donde añadir la persona: ")

    if planta not in edificio:
        print("Esa planta no existe.")
        return

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    genero = input("Género: ")

    edificio[planta]["personas"].append(
        {"nombre": nombre, "edad": edad, "genero": genero}
    )
    edificio[planta]["numero_personas"] += 1

    print(f"Persona '{nombre}' añadida a {planta}.")


def calcular_comision_total():
    total = sum(planta["comision_comunidad"] for planta in edificio.values())
    print(f"\nLa comisión total de la comunidad es: {total}€\n")


def eliminar_persona():
    planta = input("Ingrese la planta: ")
    if planta not in edificio:
        print("Esa planta no existe.")
        return

    nombre = input("Nombre de la persona a eliminar: ")

    personas = edificio[planta]["personas"]
    for p in personas:
        if p["nombre"].lower() == nombre.lower():
            personas.remove(p)
            edificio[planta]["numero_personas"] -= 1
            print(f"Persona '{nombre}' eliminada de {planta}.")
            return

    print("Esa persona no existe en esa planta.")


def cambiar_comision():
    planta = input("Ingrese la planta: ")
    if planta not in edificio:
        print("Esa planta no existe.")
        return

    nueva = float(input("Nueva comisión de comunidad: "))
    edificio[planta]["comision_comunidad"] = nueva

    print(f"Comisión de {planta} actualizada a {nueva}€.")

