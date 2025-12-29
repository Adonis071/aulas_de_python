# Tuplas são estruturas de dados muito parecidas com lista
# a principal diferênça é que as tuplas são imutáveis enquanto as listas
# são mutáveis. Podemos criar tuplas através da classe tuple,
# colocando valores separados por vírgulas entre parênteses.
frutas = ('laranja', 'pêra', 'laranja',)

letras = tuple('dados')

numeros = tuple([1, 2, 12, 90])

pais = ('Brasil', )

# Podemos acessar os valores de uma tupla da seguinte forma

frutas = ('laranja', 'pêra', 'laranja',)
print(frutas[1])  # pêra
print(frutas[2])  # laranja
print(frutas[-1])  # laranja

# podemos armazenar tuplas de tuplas (Tupla aninhada)

# Criando uma tupla aninhada
tupla = (1, 2, (3, 4, (5, 6)), 7, 8, 9)

# Acessando elementos
print(tupla[0])        # 1
print(tupla[2])        # (3, 4, (5, 6))
print(tupla[2][2][1])  # 6

# Exemplo de fatiamento (slice)
print(tupla[1:4])      # (2, (3, 4, (5, 6)), 7)
print(tupla[:3])       # (1, 2, (3, 4, (5, 6)))
print(tupla[3:])       # (7, 8, 9)
print(tupla[::2])      # (1, (3, 4, (5, 6)), 8)

# Fatiamento dentro da tupla aninhada
print(tupla[2][0:2])   # (3, 4)
print(tupla[2][2][:])  # (5, 6)


# Criando uma tupla aninhada
tupla = (1, 2, (3, 4, (5, 6)), 7, 8, 9)

# Iterando sobre os elementos da tupla principal
for elemento in tupla:
    print(elemento)

# Iterando com índice usando enumerate
for indice, elemento in enumerate(tupla):
    print(f"Índice {indice} -> {elemento}")

# Iterando dentro da tupla aninhada
for elemento in tupla[2]:
    print("Dentro da tupla interna:", elemento)

# Iterando dentro da tupla mais interna
for elemento in tupla[2][2]:
    print("Dentro da tupla mais interna:", elemento)

# Usando compreensão de lista para percorrer e transformar
quadrados = [x**2 for x in tupla if isinstance(x, int)]
print("Quadrados dos números:", quadrados)

# Iterando recursivamente (função para percorrer qualquer nível de tupla)


def percorre_tupla(t):
    for elemento in t:
        if isinstance(elemento, tuple):
            percorre_tupla(elemento)
        else:
            print("Valor encontrado:", elemento)


percorre_tupla(tupla)
