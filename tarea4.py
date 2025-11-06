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
    id:"x0002",
    "nombre":"Juan antonio",
    "edad":35,
    "genero":"M",
    "departamento":"IT",
    "sueldo":2000,
    "proyecto":{
        "nombre":"Intranet",
        "duracion_meses":6
    },
     id:"x0003",
    "nombre":"Juan antonio",
    "edad":35,
    "genero":"M",
    "departamento":"IT",
    "sueldo":2000,
    "proyecto":{
        "nombre":"Intranet",
        "duracion_meses":6
    },
      id:"x0004",
    "nombre":"Juan antonio",
    "edad":35,
    "genero":"M",
    "departamento":"IT",
    "sueldo":2000,
    "proyecto":{
        "nombre":"Intranet",
        "duracion_meses":6
    }
}
#tarea 2
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
#convertirlos en diccionarios
empleados_dict = {
     id:"x0001",
    "nombre":"Juan antonio",
    "edad":35,
    "genero":"M",
    "departamento":"IT",
    "sueldo":2000,
    "proyecto":{
        "pyhon":"en proceso",
        "calculo":"terminado",
        "pruebaDeTest":"pendiente"
    },
    id:"x0002",
    "nombre":"María López",
    "edad":28,
    "genero":"F",
    "departamento":"Marketing",
    "sueldo":1800,
    "proyecto":{
        "campañaVerano":"terminado",
        "redesSociales":"en progreso"
    },
     id:"x0003",
    "nombre":"Carlos García",
    "edad":40,
    "genero":"M",
    "departamento":"IT",
    "sueldo":2500,
    "proyecto":{
        "python":"pendiente",
        "seguridadweb":"en desarrollo"
    },
    id:"x0004",
    "nombre":"Ana Torres",
    "edad":32,
    "genero":"F",
    "departamento":"Recursos Humanos",
    "sueldo":2100,
    "proyecto":{
        "entrevistas":"terminado",
        "evaluaciones":"en revisión"
    },
    id:"x0005",
    "nombre":"Pedro Sánchez",
    "edad":45,
    "genero":"M",
    "departamento":"Compras",
    "sueldo":2300,
    "proyecto":{
        "proveedores":"terminado",
        "controlStock":"en progreso"
    },
    id:"x0006",
    "nombre":"Lucía Fernández",
    "edad":29,
    "genero":"F",
    "departamento":"Ventas",
    "sueldo":1900,
    "proyecto":{
        "ObjetivosQ1":"terminado",
        "ClientesVIP":"pendiente"
    },
    id:"x0007",
    "nombre":"David Romero",
    "edad":37,
    "genero":"M",
    "departamento":"IT",
    "sueldo":2600,
    "proyecto":{
        "python":"terminado",
        "inteligenciaArtificial":"en progreso"
    },
    id:"x0008",
    "nombre":"Sofía Navarro",
    "edad":31,
    "genero":"F",
    "departamento":"Finanzas",
    "sueldo":2200,
    "proyecto":{
        "presupuestos":"en revisión",
        "gastos2025":"pendiente"
    },
    id:"x0009",
    "nombre":"Miguel Herrera",
    "edad":42,
    "genero":"M",
    "departamento":"IT",
    "sueldo":2700,
    "proyecto":{
        "python":"en proceso",
        "servidores":"terminado"
    },
    id:"x0010",
    "nombre":"Laura Ruiz",
    "edad":34,
    "genero":"F",
    "departamento":"Diseño",
    "sueldo":2000,
    "proyecto":{
        "branding":"en progreso",
        "nuevaImagen":"terminado"
        },
           
}
for empleado in empleados_dict.values():
    if empleado==["30"]:
        print(empleado["nombre"])
for empleado in empleados_dict.values():
    if empleado["departamento"]=="IT":
        print(empleado["nombre"])