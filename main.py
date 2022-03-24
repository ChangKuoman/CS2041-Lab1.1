import csv

ruta1 = "Relación de instituciones y programas educativos.csv"
ruta2 = "Títulos registrados de Institutos de Educación Superior Tecnológicas^J Instituciones de Educación Superior 2019-2020.csv"

# Preguntas del 1 - 4

departamentos_dict = {}
lista_paginas_web = []
fechas_dict = {}
lista_centros = []

with open(ruta1, newline='', encoding="latin-1") as csv1:
    # se salta el header
    next(csv1)
    # reader
    reader = csv.reader(csv1, delimiter=',')
    for row in reader:

        # pregunta 1
        if row[26] not in departamentos_dict.keys():
            departamentos_dict[row[26]] = 1
        else:
            departamentos_dict[row[26]] += 1

        # pregunta 2
        if ".edu.pe" in row[16]:
            lista_paginas_web.append([row[3], row[16]])

        # pregunta 3
        if (row[8] == "Mujeres") and (row[37] == "Noche") and (row[39] == "Activa"):
            lista_centros.append(row[3])

        # pregunta 4
        fecha = row[40].split("-")
        if len(fecha) == 3:
            if fecha[2] not in fechas_dict.keys():
                fechas_dict[fecha[2]] = 1
            else:
                fechas_dict[fecha[2]] += 1



# 1. Indique los 3 departamentos que cuentan con más locales educativos.
cantidad_departamento = sorted(departamentos_dict.items(), key=lambda x: x[1], reverse=True)[0:3]
print("Departamentos con más locales educativos:")
for i in range(3):
    print(f"({i+1}) Departamento: {cantidad_departamento[i][0]}. Cantidad: {cantidad_departamento[i][1]}")

print("\n-----\n")

# 2. Liste aquellos centros educativos que cuenten con una página web y su dominio termine en ’.edu.pe’.
print("Lista de centros educativos que cuentas con pagina web y dominio .edu.pe:")
for i in lista_paginas_web:
    print(f"Centro educativo: {i[0]}. Pagina web: {i[1]}")

print("\n-----\n")

# 3 Identifique aquellos centros educativos que permitan solo mujeres, donde el turno sea de noche y no esten inhabilitados.
print("Centros educativos que permitan solo mujeres, donde el turno sea de noche y no esten inhabilitados.")
for i in lista_centros:
    print(f"Centro educativo: {i}")

print("\n-----\n")

# 4. ¿En qué año se crearon más centros educativos?
anho_mas_centros = sorted(fechas_dict.items(), key=lambda x: x[1], reverse=True)[0]
print(f"El anho con mas centros educativos fue {anho_mas_centros[0]} con {anho_mas_centros[1]} creados.")

print("\n-----\n")

