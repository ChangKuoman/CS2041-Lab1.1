import csv

ruta1 = "Relación de instituciones y programas educativos.csv"
ruta2 = "Títulos registrados de Institutos de Educación Superior Tecnológicas^J Instituciones de Educación Superior 2019-2020.csv"

# Preguntas del 1 - 4

departamentos_dict = {}
lista_paginas_web = []

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


# 1. Indique los 3 departamentos que cuentan con más locales educativos.
cantidad_departamento = sorted(departamentos_dict.items(), key=lambda x: x[1], reverse=True)[0:3]
print("Departamentos con más locales educativos:")
for i in range(3):
    print(f"({i+1}) Departamento: {cantidad_departamento[i][0]}. Cantidad: {cantidad_departamento[i][1]}")


# 2. Liste aquellos centros educativos que cuenten con una página web y su dominio termine en ’.edu.pe’.
print("Lista de centros educativos que cuentas con pagina web y dominio .edu.pe:")
for i in lista_paginas_web:
    print(f"Centro educativo: {i[0]}. Pagina web: {i[1]}")
