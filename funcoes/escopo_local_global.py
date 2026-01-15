# Em Python, variáveis podem ter diferentes escopos, ou seja, diferentes "alcances" dentro do código.
# Os dois principais são: escopo local e escopo global.

# Escopo global:
# - Variáveis declaradas fora de funções pertencem ao escopo global.
# - Podem ser acessadas em qualquer parte do código, inclusive dentro de funções.
# - Porém, se uma variável global for modificada dentro de uma função sem a palavra-chave 'global',
#   o Python cria uma nova variável local, sem alterar a global.

# Escopo local:
# - Variáveis declaradas dentro de uma função pertencem ao escopo local.
# - Só existem e podem ser acessadas dentro da função onde foram criadas.
# - Após o término da execução da função, essas variáveis deixam de existir.

# Exemplo de escopo global
x = 10  # variável global


def mostrar_global():
    print(x)  # acessa a variável global


mostrar_global()  # saída: 10

# Exemplo de escopo local


def mostrar_local():
    y = 5  # variável local
    print(y)


mostrar_local()  # saída: 5
# print(y) → gera erro, pois 'y' só existe dentro da função

# Exemplo de conflito entre escopo global e local
z = 20  # variável global


def alterar():
    z = 99  # cria uma variável local, não altera a global
    print("Dentro da função:", z)


alterar()          # saída: Dentro da função: 99
print("Fora da função:", z)  # saída: Fora da função: 20

# Usando a palavra-chave 'global' para alterar variável global dentro da função
a = 50


def alterar_global():
    global a
    a = 100  # altera a variável global
    print("Dentro da função:", a)


alterar_global()       # saída: Dentro da função: 100
print("Fora da função:", a)  # saída: Fora da função: 100

# Em resumo:
# - Escopo global: variáveis acessíveis em todo o programa.
# - Escopo local: variáveis criadas dentro de funções e acessíveis apenas nelas.
# - A palavra-chave 'global' permite modificar variáveis globais dentro de funções.
