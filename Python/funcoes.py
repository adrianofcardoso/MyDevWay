#Criar uma função
'''
Resumo:
Você tera def chamando a função onde você atribui o nome da função = f
e dentro do parenteses você coloca o parametro que você quer passar para a função, nesse caso x.

Ideia de função:
Uma boa prática de código é que a função serve para contar somente oque ela é, é interessante que ela não receba inputs e etc
como no exemplo de EhPar(), ela calcula somente se é par ou impar, ela não recebe o input() do usuário 


Funcionamento do def:
Ele atua mais ou menos como um script.

Return: 
Significa que a função irá retornar um valor, ou seja, quando a função for chamada, ela irá 
retornar o valor que está depois do return, nesse caso 1 + x.
'''
#%%
def f(x):
    return 1 + x

#%% Função base
def juros_compostos(anos):
    return 1000 * 1.13 ** anos

juros_compostos(2)

#%% Passando mais elementos na função

def juros(aporte: float, taxa: float, anos: int)->float:
    '''
    Isso é um docstring, ou seja, um comentário que explica o que a função faz.
    Sempre que eu quiser reutiliza-la e passar o mouse em cima aparecerá essa explicação.

    para declarar o tipo da variável, basta colocar o nome da variável, dois pontos e o tipo da variável.

    aporte = recebe um float valor inicial de investimento
    
    taxa = taxa de juros recebendo um float
    
    anos = recebe um int quantidade de anos que o investimento irá durar
    '''
    return aporte * (1 + taxa) ** anos

resultado = juros(aporte = 1000, taxa = 0.13, anos = 2)
print("Seu retorno financeiro é:", resultado)

#%% Função EhPar ou EhImpar

def EhPar (numero: int):
    if numero % 2 == 0:
        print("Eh par")
    else:
        print("Eh impar")

numero = int(input("Insira o valor para verificar se é par: "))
EhPar (numero)

'''
Ideia de função:
Uma boa prática de código é que a função serve para contar somente oque ela é, é interessante que ela não receba inputs e etc
como no exemplo de EhPar(), ela calcula somente se é par ou impar, ela não recebe o input() do usuário 

Return: Serve para você armazenar algum valor e retornar isso para o usuario.
Print: Serve para você eixbir um valor para o usuario
'''
#%%
def EhPar (numero: int):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

numero = int(input("Insira o valor para verificar se é par: "))
EhPar (numero)

resultado = EhPar(numero)

print("O restuldao é:", numero, "e ele é:", resultado)

#%%
def soma (a: float, b: float)->float:
    return a + b

def media (a:float, b:float)->float:
    return soma(a,b) / 2

a = int(input("Insira o primeiro valor para ser somado: "))
b = int(input("Insira o segundo valor para ser somado:"))

print ("A media desses numeros eh: ", media(a,b))

'''
OBSERVAÇÕES:
Argumentos opcionais sempre devem estar DEPOIS de argumentos obrigatorios.
'''

#TOPICO IMPORTANTE SOBRE *ARGS
'''
Em resumo é uma tupla que argamazena 0 ou infinitos valores a partir de outros elementos obrigatorios.
 Isso pode me ajudar quando eu tiver que inserir elementos futuros 
'''

#%%
def soma (a:float, b:float, *args)->float:
    valores = [a, b, *args]  
    return sum(valores)

def media (a:float, b:float, *args)->float:
    return soma(a, b, *args) / (len(args) + 2)

a = float(input("Insira o a valor para ser somado: "))
b = float(input("Insira o b valor para ser somado: "))
c = float(input("Insira o c valor para ser somado: "))

print("A media é: ", media(a,b,c))
# %%

#TERMINAR DE ASSISTIR A AULA (https://www.youtube.com/watch?v=JZlJ1otXBD8&list=PLvlkVRRKOYFSpRkqnR0p2A-eaVlpLnN3D&index=10)