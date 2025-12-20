frutas = []
print(frutas)

frutas = ['banana', 'abacaxi']
print(frutas)


letras = list('Adonis')
print(letras)

numeros = list(range(20))
print(numeros)

carro = ['Ferrari', 'F8', 20000000, 2025, 1900, 'São Paulo', True]
print(carro)

# Métodos de acessos das listas a cima usando seus índices que são contados apartir do índice zero:
print(frutas[0])

print(letras[2])

print(numeros[7])

print(carro[5])

# listas aninhadas ou bidimensionais (Tabelas):

tabela = [
    ['Adonis', 90, 9],
    ['Computador', 700, 0],
    ['Gato', 'Estudar', 800]
]
print(tabela)
# Métodos de acessar  uma lista aninhada
uma_linha = tabela[0]
linha1_coluna1 = tabela[0][0]
linha2_coluna2 = tabela[1][1]
ultima_linha_ultima_coluna = tabela[-1][-1]

print(uma_linha)
print(linha1_coluna1)
print(linha2_coluna2)
print(ultima_linha_ultima_coluna)

# Fatiamento de listas podemos extrair conjunto de valores de uma  sequência.

lista = ['A', 'D', 'O', 'N', 'I', 'S']


lista[2:]  # ['O', 'N', 'I', 'S']
lista[:2]  # ['A', 'D']
lista[2:6]  # ['O', 'N', 'I', 'S']
lista[0:2:5]  # ['A']
lista[::]  # ['A', 'D', 'O', 'N', 'I', 'S']
lista[::-1]  # ['S', 'I', 'N', 'O', 'D', 'A']

# para percorrer uma lista podemoas usar o comando for, por exemplo.

animais = ['cobra', 'lagarto', 'Gato', 'Cachorro']

for animal in animais:
    print(animal)

# percorrendo lista usando o enumerate:

animais = ['cobra', 'lagarto', 'Gato', 'Cachorro']

for indice, animal in enumerate(animais):
    print(f'{indice} : {animal}')

# compreensão de listas, e usado para gerar uma lista apartir de uma lista já existente OBS(se for salvar a lista
# tem que usar uma lista vazia e usar o método append()):
numeross = [1, 2, 9, 5, 6, 10, 60, 0, 2]
# nossa nova lista
pares = [num for num in numeross if num % 2 == 0]
print(pares)

# Outra forma de criarmos uma lista apartir de uma existente:
numeross = [1, 2, 9, 5, 6, 10, 60, 0, 2]
# Como citado na observação. Versão tradicional

quadrado = []


for num in numeross:
    quadrado.append(num ** 2)
