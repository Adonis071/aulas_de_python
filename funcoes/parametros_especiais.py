"""Em Python existem parâmetros especiais que controlam como os argumentos podem ser 
passados para uma função, tornando o código mais claro e seguro. O símbolo / define 
parâmetros somente posicionais, ou seja, eles devem ser informados pela ordem e não 
podem ser chamados pelo nome. Isso é útil quando você não quer que o usuário dependa
 dos nomes internos da função. Já o símbolo * define parâmetros somente nomeados, que
   obrigatoriamente precisam ser passados usando o nome do argumento, garantindo clareza
	 na chamada da função. É possível combinar os dois em uma mesma definição, criando 
	 regras explícitas de uso. Exemplos
"""

# Parâmetros somente posicionais


def dividir(a, b, /):
    return a / b


print(dividir(10, 2))        # 5.0
# dividir(a=10, b=2) → gera erro

# Parâmetros somente nomeados


def cadastrar(*, nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")


cadastrar(nome="Adonis", idade=25)
# cadastrar("Adonis", 25) → gera erro

# Mistura de posicionais, flexíveis e nomeados


def exemplo(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


exemplo(1, 2, 3, d=4, e=5, f=6)

"""Nesse último caso, a e b só podem ser posicionais, c e d podem 
ser posicionais ou nomeados, e e e f só podem ser nomeados. Em resumo, os parâmetros 
especiais (/ e *) ajudam a definir regras claras de como os argumentos devem ser 
passados, evitando ambiguidades e tornando funções mais legíveis e seguras.
"""
