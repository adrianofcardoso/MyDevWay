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

#%% Criando um contador de numeros em uma lista de numeros

lista = [0,1,2,1,1,5,3,4,5,6,1,2,3,7,6,7,8,8,9,9]


numero = int(input("Digite um numero para contar: "))
numero = int(numero) 


contador = 0 
for i in lista:
    if i == numero:
        contador += 1

print(f"O numero {numero} aparece {contador} vezes na lista.")

#%% Trabalhando com adição de elementos em uma lista

idades = []

while True:
    idade = input("Digite uma idade: ")
    if idade == "":
        break
    idades.append(int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print (idades)
print(f"Média: {media}")
print(f"Mínimo: {minimo}") 
print(f"Máximo: {maximo}")
print(f"Quantidade: {qtde}")
