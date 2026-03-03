# print("Ola mundo! Este é o Python")
Aqui armazeno toda a minha base de aprendizagem (com o tempo irei atualizando e colocando mais materiais e fontes.)

---

## 📚 Documentação Python 
- [Documentação Official Python](https://docs.python.org/3/using/index.html)
- [Documentação Python do W3Schools](https://www.w3schools.com/python/)

---

## Youtube 
 - Dados:

[Teo Me Why](https://www.youtube.com/watch?v=OeKzVjiiRm4&list=PLvlkVRRKOYFSpRkqnR0p2A-eaVlpLnN3D)

---

## Operadores Matématicos no Python:
'''python
*Básicos:*

"+" -> Adição,

"-" -> Subtração,

"/" -> Divisão (Float),

"//" -> Divisão (Int),

"%" -> Resto da divisão. Exemplo: % 2 == 0 Isso indica se o programa é par ou impar.,

"*" -> Multiplicação, 

"**" -> Exponenciação

*Atribuição Matemática:*

+= -> Soma e atribui (x +=5 isso é igual a x+5)

-= -> Substrai e atribui

*= (Multiplica e atribui)

/= (Divide e atribui)

//= (Divide inteiro e atribui)

%= (Calcula o módulo e atribui)

**= (Eleva à potência e atribui)

Nota: Se você precisar de operações matemáticas mais complexas (como raiz quadrada, seno, cosseno, logaritmos, etc.), o Python possui um módulo nativo chamado math. Você não usa um operador simples para eles, mas sim importa a biblioteca usando import math.
'''

---

## 🤓 Observações e Aprendizados:

- Diferença entre listas e tuplas:
    Basicamente as *Listas* trabalham com dados mutaveis ou seja dados que podem sofrer alterações no futuro, normalmente se utiliza [] possui diversos métodos que se podem trabalhar com ela, como: .append(), .remove().

    Utilidade: Muito útil para trabalhar com dados homogeneos (dados do mesmo tipo) e dados que podem sofrer alteração no futuro.

    Comum uso:
    ¹ Um carrinho de compras de um e-commerce onde itens são adicionados e removidos.
    ² Filas e Pilhas: Quando você tem uma lista de tarefas pedentes a serem feitas e precisa atualiza-las, conceito esse utilizado em um de meus projetos [Task Tracker CLI](https://github.com/adrianofcardoso/task-tracker-CLI).
    ³ Iterações e Filtragem: Quando você quer ler um arquivo com dados extensos e salvar arquivos especificos.

    Já as *Tuplas* são o oposto, é para dados imutaveis, ou seja não tem como você altera-lo, remover e etc, normalmente se utiliza (), tamanho fixo e normalmente utilizam menos memorias que as listas, funcionando de forma mais rápida. Como: informações sensiveis ou dados pessoais.

    Utilidade: 
    ¹ Quando queremos garrantir que certos dados não serão alterados por outra parte do codigo.
    ² Quando uma função precisa retornar mais de um valor.
    ³ Chaves de um dicionario ([10, 20] "Numero":)

---