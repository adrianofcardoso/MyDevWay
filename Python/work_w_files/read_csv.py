import math 

#%%
archive = "data.csv"

with open(archive) as open_file:
    cabecalho = open_file.readlines()
    for lines in cabecalho:
        print(lines)

#%%
dados = dict()

chaves = cabecalho[0].strip("\n").split(";")
for c in chaves:
    dados[c] = []

for lines in cabecalho[1:]:

    elementos = lines.strip("\n").split(";")
    
    for i in range(len(elementos)):

        dados[chaves[i]].append(elementos[i])

#forma pytonica de fazer o mesmo processo acima
idades = [int(i) for i in dados["idade"]]
media = sum(idades) / len(idades)
media

#%%
'''
idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades) / len(idades)
media
'''
