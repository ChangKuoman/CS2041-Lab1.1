import csv
from math import pi, cos, sqrt

ruta1 = "Relación de instituciones y programas educativos.csv"
ruta2 = "Títulos registrados de Institutos de Educación Superior Tecnológicas^J Instituciones de Educación Superior 2019-2020.csv"

# Preguntas del 1 - 4 y 8

departamentos_dict = {}
lista_paginas_web = []
fechas_dict = {}
lista_centros = []
matriz_datos = []

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

        # pregunta 8
        matriz_datos.append(row)

# problemas 5 - 8

diccionario = {}
centro_tit = {}
cantidad_titulos_departamento = {}

with open(ruta2, newline='', encoding="latin-1") as csv2:
    next(csv2)
    reader = csv.reader(csv2, delimiter=';')
    for row in reader:
        # problema 5
        if row[1] not in diccionario.keys():
            diccionario[row[1]] = 1
        else:
            diccionario[row[1]] += 1
        # problema 6
        if row[10] not in centro_tit.keys():
            centro_tit[row[10]] = 1
        else:
            centro_tit[row[10]] += 1
        # problema 7
        if row[2] not in cantidad_titulos_departamento.keys():
            cantidad_titulos_departamento[row[2]] = 1
        else :
            cantidad_titulos_departamento[row[2]] += 1

print("\n---PROBLEMA 1---\n")

# 1. Indique los 3 departamentos que cuentan con más locales educativos.
cantidad_departamento = sorted(departamentos_dict.items(), key=lambda x: x[1], reverse=True)[0:3]
print("Departamentos con más locales educativos:")
for i in range(3):
    print(f"({i+1}) Departamento: {cantidad_departamento[i][0]}. Cantidad: {cantidad_departamento[i][1]}")

print("\n---PROBLEMA 2---\n")

# 2. Liste aquellos centros educativos que cuenten con una página web y su dominio termine en ’.edu.pe’.
print("Lista de centros educativos que cuentas con pagina web y dominio .edu.pe:")
for i in lista_paginas_web:
    print(f"Centro educativo: {i[0]}. Pagina web: {i[1]}")

print("\n---PROBLEMA 3---\n")

# 3 Identifique aquellos centros educativos que permitan solo mujeres, donde el turno sea de noche y no esten inhabilitados.
print("Centros educativos que permitan solo mujeres, donde el turno sea de noche y no esten inhabilitados.")
for i in lista_centros:
    print(f"Centro educativo: {i}")

print("\n---PROBLEMA 4---\n")

# 4. ¿En qué año se crearon más centros educativos?
anho_mas_centros = sorted(fechas_dict.items(), key=lambda x: x[1], reverse=True)[0]
print(f"El anho con mas centros educativos fue {anho_mas_centros[0]} con {anho_mas_centros[1]} creados.")

print("\n---PROBLEMA 5---\n")

# 5. ¿Quién es el director que emitió más títulos y desde qué centro educativo?
total = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)[0:3]
for i in range(3):
    print(f"({i+1}) Nombre de la Institucion: {total[i][0]}. Cantidad: {total[i][1]}")

nombre={}
with open(ruta1, newline='', encoding="latin-1") as csv1:
    # se salta el header
    next(csv1)
    # reader
    reader = csv.reader(csv1, delimiter=',')
    for row in reader:
        if row[3] == total[0][0]:
            nombre_director = row[13]
            break

print(f"El director que emitio mas titulos es {nombre_director} en la institucion de {total[0][0]}")

print("\n---PROBLEMA 6---\n")

# 6. ¿Que carrera tecnica es la mas demandada, es decir aquel que emitio mas tıtulos
cantidad_titulos_carrera = sorted(centro_tit.items(), key=lambda x: x[1], reverse = True)[0:3]
print("Carrera con mas titulos emitidos (mas demandada) es: ")
for i in range(1):
    print(f"{cantidad_titulos_carrera[i][0]} con {cantidad_titulos_carrera[i][i+1]} titulos emitidos.")
csv2.close()

print("\n---PROBLEMA 7---\n")

# 7. Obtenga un resumen de la cantidad de titulos registrados por departamento.

print("Cantidad de titulos registrados por departamento.")
titulos_por_departamento = sorted(cantidad_titulos_departamento.items(), key=lambda x: x[1], reverse = True)[0:25]
for i in range(25):
    print(f"Departamento: {titulos_por_departamento[i][0]}. Cantidad: {titulos_por_departamento[i][1]}")

print("\n---PROBLEMA 8---\n")

# 8. ¿Es posible saber qué centros educativos están muy alejados uno del otro?
def distancia(lat1, lat2, long1, long2):

    delta_lat = lat1 * pi / 180 - lat2 * pi / 180
    delta_long = long1 * pi / 180 - long2 * pi / 180
    prom_lat = (lat1 * pi / 180 + lat2 * pi / 180)/2.0
    d = 6371.009 * sqrt(delta_lat ** 2 + (delta_long * cos(prom_lat)) ** 2)

    return d

mayor_dist = 0
centro1 = matriz_datos[0][3]
centro2 = ""

for i in matriz_datos:
    d = distancia(float(matriz_datos[0][32]), float(i[32]), float(matriz_datos[0][33]), float(i[33]))
    if d > mayor_dist:
        mayor_dist = d
        centro2 = i[3]
print(f"Ejemplo:\nLa mayor distancia del centro educativo {centro1} es con el {centro2} y es {mayor_dist}.")

# problema 8 con input

mayor_dist = 0
cod_mod = input('Ingrese el cod_mod de la IE a analizar (ej: "0210435", "1222157"): ')
centro1 = ""
centro2 = ""
k = 0

for i, lista in enumerate(matriz_datos):
    if lista[0] == cod_mod:
        centro1 = lista[3]
        k = i
        break
print(f"Colegio con cod_mod {cod_mod}: {centro1}")

for i in matriz_datos:
    d = distancia(float(matriz_datos[k][32]), float(i[32]), float(matriz_datos[k][33]), float(i[33]))
    if d > mayor_dist:
        mayor_dist = d
        centro2 = i[3]

print(f"El centro educativo mas lejano a {centro1} es: {centro2}, y estan separados por {mayor_dist} Km")
