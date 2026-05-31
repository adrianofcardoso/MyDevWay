import math

#%%
csv_filename = "data.csv"

with open(csv_filename) as open_file:
    cabecalho = open_file.readlines()
    for lines in cabecalho:
        print(lines)

#%%
csv_data_dict = dict()

chaves = cabecalho[0].strip("\n").split(";")
for column_name in chaves:
    csv_data_dict[column_name] = []

for lines in cabecalho[1:]:

    elementos = lines.strip("\n").split(";")
    
    for element_index in range(len(elementos)):

        csv_data_dict[chaves[element_index]].append(elementos[element_index])

#forma pytonica de fazer o mesmo processo acima
idades = [int(i) for i in csv_data_dict["idade"]]
media = sum(idades) / len(idades)
media

#%%
'''
idades = []
for i in csv_data_dict["idade"]:
    idades.append(int(i))

media = sum(idades) / len(idades)
media
'''
