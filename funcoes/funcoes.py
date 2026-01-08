"""Funções em Python são blocos de código reutilizáveis que executam uma tarefa específica.
  Elas são definidas com a palavra-chave def, seguidas de um nome, parâmetros opcionais 
 e um corpo de instruções. O uso de funções traz organização, evita repetição de código,
  melhora a legibilidade e facilita a manutenção. Uma função pode ou não retornar valores
  usando return. Existem funções definidas pelo usuário, funções embutidas como len(), 
 print() e sum(), e funções anônimas chamadas lambda. Exemplo: """


def soma(a, b):
    return a + b


print(soma(5, 3))  # 8


def mensagem():
    print("Olá, seja bem-vindo ao Python!")


mensagem()  # Olá, seja bem-vindo ao Python!

# funções com parâmetros: OBS se não passar um nome para a função
# que espera este argumento o python lançará uma exceção.


def saudacao(nome):
    print(f"Olá, {nome}!")


saudacao("Adonis")
saudacao("Maria")

# Retornando duas operações


def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    return soma, subtracao


resultado = operacoes(10, 4)
print(resultado)        # (14, 6)
print(resultado[0])     # 14
print(resultado[1])     # 6

"""Maneira mais clara: desempacotamento
Em vez de acessar por índice, podemos desempacotar os valores diretamente em variáveis:
"""


def operacoes(a, b):
    return a + b, a - b


soma, subtracao = operacoes(10, 4)
print("Soma:", soma)  # Soma: 14
print("Subtração:", subtracao)  # Subtração: 6

# Função com valor padrão


def apresentar(nome, idade=18):
    print(f"Nome: {nome}, Idade: {idade}")


apresentar("João")  # Nome: João, Idade: 18
apresentar("Maria", 25)  # Nome: Maria, Idade: 25

"""- Argumentos nomeados (ou keyword arguments) são aqueles em que você especifica o nome do parâmetro ao chamar a função.
- Isso torna o código mais legível e evita erros de ordem dos parâmetros.
"""


def apresentar(nome, idade, curso):
    print(f"Nome: {nome}, Idade: {idade}, Curso: {curso}")


# Chamando com argumentos posicionais
apresentar("João", 20, "Engenharia")
# Nome: João, Idade: 20, Curso: Engenharia


# Chamando com argumentos nomeados
apresentar(nome="Maria", idade=22, curso="Medicina")
# Nome: Maria, Idade: 22, Curso: Medicina

"""Argumentos nomeados em Python são aqueles em que você 
especifica o nome do parâmetro ao chamar a função, tornando o 
código mais claro e flexível. Eles permitem mudar a ordem dos 
argumentos e deixam explícito qual valor corresponde a cada 
parâmetro. A principal desvantagem é que tornam o código mais
 verboso, dependem dos nomes definidos na função (se o nome mudar,
   todas as chamadas precisam ser ajustadas), podem ser redundantes 
   em funções simples e, em casos de uso muito frequente, têm 
   desempenho ligeiramente inferior em comparação com argumentos
     posicionais. Em resumo, são ótimos para clareza e segurança, 
     mas devem ser usados
 com equilíbrio para não comprometer a legibilidade."""

"""O que são
- *args → usado para passar um número variável de argumentos posicionais para uma função.
- **kwargs → usado para passar um número variável de argumentos nomeados (keyword arguments).
Eles tornam as funções mais flexíveis, permitindo receber quantos parâmetros forem necessários 
sem precisar definir todos na assinatura."""


def soma(*args):
    return sum(args)


print(soma(1, 2, 3))       # 6
print(soma(10, 20, 30, 40))  # 100

"""Aqui, args é uma tupla com todos os valores passados.

2. Usando ** kwargs(argumentos nomeados variáveis)"""


def apresentar(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


apresentar(nome="João", idade=20, curso="Engenharia")


""" Aqui, kwargs é um dicionário com os pares chave/valor.
Saída:
nome: João
idade: 20
curso: Engenharia


3. Misturando * args e ** kwargs"""


def exemplo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


exemplo(1, 2, 3, nome="Maria", idade=22)


"""Saída:
args: (1, 2, 3)
kwargs: {'nome': 'Maria', 'idade': 22}


 Resumindo
- *args → recebe múltiplos valores como tupla.
- **kwargs → recebe múltiplos argumentos nomeados como dicionário.
- Juntos, deixam funções mais genéricas e reutilizáveis.
 Quer que eu monte alguns exercícios práticos para você treinar
   *args e **kwargs na prática?"""


def apresentar(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


apresentar(nome="João", idade=20, curso="Engenharia")

# Aqui, kwargs é um dicionário com os pares chave/valor.

"""Misturando *args e **kwargs
"""


def exemplo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


exemplo(1, 2, 3, nome="Maria", idade=22)

"""SAIDA
args: (1, 2, 3)
kwargs: {'nome': 'Maria', 'idade': 22}"""
