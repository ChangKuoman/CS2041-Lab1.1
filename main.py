
archivo1 = "Títulos registrados de Institutos de Educación Superior Tecnológicas^J Instituciones de Educación Superior 2019-2020.csv"

dict = {}

import csv
with open(archivo1, newline='', encoding="utf-8") as csvfile:
   next(csvfile)
   spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
   for row in spamreader:
       if row[2] not in dict.keys():
           dict[row[2]] = 1
       else:
           dict[row[2]] += 1

matriz1_1 = []
for i,j in dict.items():
    matriz1_1.append([i, j])

matriz1_1.sort(key = lambda x:x[1], reverse=True)

for i in range(3):
    print(f"Departamento: {matriz1_1[i][0]}. Cantidad: {matriz1_1[i][1]}")







# print(data1.head())

# data2 = pd.read_csv("Relación de instituciones y programas educativos.csv", encoding="latin-1")

# print(data2.head())
