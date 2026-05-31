#%%
text_filename = "history.txt"

with open(text_filename) as open_file:
    conteudo = open_file.read()

print(conteudo)

'''
Jeito arcaico de fazer

#Abre arquivo para leitura
open_file = open(text_filename)

#Lê o conteúdo do arquivo
conteudo = open_file.read()
print(conteudo)

#Fecha o arquivo
open_file.close()
'''
# %%
