# Em Python, funções são consideradas objetos de primeira classe.
# Isso significa que elas podem ser manipuladas como qualquer outro dado:
# - Podem ser atribuídas a variáveis
# - Podem ser passadas como argumentos para outras funções
# - Podem ser retornadas por funções
# - Podem ser armazenadas em estruturas como listas e dicionários
# Esse conceito é fundamental porque amplia a flexibilidade da linguagem
# e possibilita técnicas avançadas como funções de ordem superior,
# decoradores e programação funcional.

# Exemplo 1: atribuir função a variável
def saudacao(nome):
    return f"Olá, {nome}!"


msg = saudacao
print(msg("Adonis"))  # Olá, Adonis!

# Exemplo 2: passar função como argumento


def executar(funcao, valor):
    return funcao(valor)


def quadrado(x):
    return x**2


print(executar(quadrado, 5))  # 25

# Exemplo 3: retornar função


def criar_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar


dobro = criar_multiplicador(2)
print(dobro(10))  # 20

# Exemplo 4: armazenar funções em estruturas


def soma(a, b): return a + b
def subtracao(a, b): return a - b


operacoes = {"somar": soma, "subtrair": subtracao}
print(operacoes["somar"](10, 5))     # 15
print(operacoes["subtrair"](10, 5))  # 5

# Em resumo, tratar funções como objetos de primeira classe significa
# que elas podem ser manipuladas como valores comuns, o que amplia muito
# o poder da linguagem e permite escrever programas mais expressivos,
# reutilizáveis e organizados.
