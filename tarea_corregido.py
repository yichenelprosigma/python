empleado={
    id:"x0001",
    "nombre":"Juan antonio",
    "edad":35,
    "genero":"M",
    "departamento":"IT",
    "sueldo":2000,
    "proyecto":{
        "nombre":"Intranet",
        "duracion_meses":6 
        },
}

empleados = [

["X001", "Juan Antonio", 35, "hombre", "IT", 2000, {"python":"en proceso","calculo":"terminado","pruebaDeTest":"pendiente"}],

["X002", "María López", 28, "mujer", "Marketing", 1800, {"campañaVerano":"terminado","redesSociales":"en progreso"}],

["X003", "Carlos García", 40, "hombre", "IT", 2500, {"python":"pendiente","seguridadweb":"en desarrollo"}],

["X004", "Ana Torres", 32, "mujer", "Recursos Humanos", 2100, {"entrevistas":"terminado","evaluaciones":"en revisión"}],

["X005", "Pedro Sánchez", 45, "hombre", "Compras", 2300, {"proveedores":"terminado","controlStock":"en progreso"}],

["X006", "Lucía Fernández", 29, "mujer", "Ventas", 1900, {"ObjetivosQ1":"terminado","ClientesVIP":"pendiente"}],

["X007", "David Romero", 37, "hombre", "IT", 2600, {"python":"terminado","inteligenciaArtificial":"en progreso"}],

["X008", "Sofía Navarro", 31, "mujer", "Finanzas", 2200, {"presupuestos":"en revisión","gastos2025":"pendiente"}],

["X009", "Miguel Herrera", 42, "hombre", "IT", 2700, {"python":"en proceso","servidores":"terminado"}],

["X010", "Laura Ruiz", 34, "mujer", "Diseño", 2000, {"branding":"en progreso","nuevaImagen":"terminado"}]

]

empleadosDiccionario = {}
for empleado in empleados:
    empleadosDiccionario[empleado[0]] = {
        "nombre": empleado[1],
        "edad": empleado[2],
        "genero": empleado[3],
        "departamento": empleado[4],
        "sueldo": empleado[5],
        "proyectos": empleado[6]
    }
for id, datos in empleadosDiccionario.items():
    print(id,"=>", datos)
print(empleadosDiccionario)

if datos["edad"]>35:
    print(datos["Nombre"],"-",datos["edad"],"años")
# if datos["proyectos"]["python"]=="en proceso":
#     print(datos["nombre"],"- Proyecto Python:",datos["proyectos"]["python"])

empleadosDiccionario["X011"] = {
     "nombre": "Carmen Díaz",
     "edad": 30,
     "genero": "mujer",
     "departamento": "IT",
     "sueldo": 2400,
     "proyectos": {"python": "pendiente", "appMovil": "en desarrollo"}
}
for id, datos in empleadosDiccionario.items():
    print(id,"=>", datos)
for id, datos in empleadosDiccionario.items():
    datos["sueldo"] += 200
    print(f"sueldo actualizado de {datos['nombre']}: {datos['sueldo']}")
for id, datos in empleadosDiccionario.items():
    print(id,"=>", datos)