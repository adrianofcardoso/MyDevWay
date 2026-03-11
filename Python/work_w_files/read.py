#%%
name_archive = "history.txt"

with open(name_archive) as open_file:
    conteudo = open_file.read()

print(conteudo)

'''
Jeito arcaico de fazer

#Abre arquivo para leitura
open_file = open(name_archive)

#Lê o conteúdo do arquivo
conteudo = open_file.read()
print(conteudo)

#Fecha o arquivo
open_file.close()
'''
# %%
