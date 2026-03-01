#Criar uma função
'''
Resumo:
Você tera def chamando a função onde você atribui o nome da função = f
e dentro do parenteses você coloca o parametro que você quer passar para a função, nesse caso x.

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

juros(aporte = 1000, taxa = 0.13, anos = 2)

juros()

#TERMINAR DE ASSISTIR A AULA (https://www.youtube.com/watch?v=JZlJ1otXBD8&list=PLvlkVRRKOYFSpRkqnR0p2A-eaVlpLnN3D&index=9)