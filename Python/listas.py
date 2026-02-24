#%% Criando uma lista de idades
idade = [18, 20, 22, 25, 30, 35, 40, 50]

# tamanho da lista len() 

print(idade[0])  # Acessa o primeiro elemento da lista
print("Soma das idades:", sum(idade))  # Soma de todas as idades
print("Média das idades:", sum(idade) / len(idade))  # Média das idades

#%% Listar lista dentro de outra lista

Adriano = ["Adriano", 
           30, 
           "Engenheiro",
           ["Python", "Java", "C++", "C#", "JavaScript"]]

'''
Erro cometido:
eu coloquei na posição 0 da lista mas na verdade se eu quero acessa a lista de lista
eu preciso colocar a posição da segunda lista e depois a posição do elemento dentro da segunda lista
'''
Adriano[3][-1]  # Acessa o nome e o primeiro elemento da segunda lista

tamanho = len(Adriano)
pos = tamanho -1
lang = Adriano[pos]
Adriano[pos][len(lang) -1]

Adriano[-1][2:5]
Adriano[-1][5:]  # Acessa os elementos de índice 2 a 4 da segunda lista