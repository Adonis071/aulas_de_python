# União entre os conjuntos
conjunto_a = {1, 2}
conjunto_b = {5, 6}
print(conjunto_a.union(conjunto_b))  # {1, 2, 5, 6}

# Nos trás a intersecção entre os conjuntos

conjunto_c = {1, 2, 5, 6}
conjunto_d = {5, 6, 8, 9}
print(conjunto_c.intersection(conjunto_d))  # {5, 6}

# Diferença entre os conjuntos
conjunto_e = {1, 2, 5, 6, 7, 8}
conjunto_f = {2, 1, 6, 0, 10, 9}
conjunto_g = {1, 2, 5, 6}

print(conjunto_e.difference(conjunto_f))
# {8, 5, 7} nos tras só oque está em seu conjunto menos o conjunto f

print(conjunto_f.difference(conjunto_e))
# {0, 9, 10}nos tras só oque está em seu conjunto menos o conjunto e

print(conjunto_e.symmetric_difference(conjunto_f))
# {0, 5, 7, 8, 9, 10} Nos tras todos os elementos que não estão na intersecção

print(conjunto_e.issubset(conjunto_g))
# False todos os elementos donconjunto e estão em conjunto g (NÃO)

print(conjunto_g.issubset(conjunto_e))
# True todos os elementos que estão em g estão presentes no conjunto e (SIM)

A = {1, 2, 3, 4, 5}
B = {2, 3}
C = {6, 7}

print(A.issuperset(B))  # True → A contém todos os elementos de B
print(A.issuperset(C))  # False → A não contém os elementos de C
print(B.issuperset(A))  # False → B não contém todos os elementos de A

A = {1, 2, 3}
B = {4, 5, 6}
C = {3, 4, 5}

print(A.isdisjoint(B))  # True → não há elementos em comum
print(A.isdisjoint(C))  # False → ambos têm o elemento 3

# Criando um conjunto
numeros = {1, 2, 3}

# Adicionando um novo elemento
numeros.add(4)
print(numeros)   # {1, 2, 3, 4}

# Tentando adicionar um elemento já existente
numeros.add(2)
print(numeros)   # {1, 2, 3, 4}  (não duplica)

# Criando um conjunto
numeros = {1, 2, 3, 4, 5}

# Limpando o conjunto
numeros.clear()

print(numeros)   # Saída: set()

# Criando um conjunto
A = {1, 2, 3, 4}

# Fazendo uma cópia
B = A.copy()

print(A)  # {1, 2, 3, 4}
print(B)  # {1, 2, 3, 4}

# Alterando o conjunto original
A.add(5)

print(A)  # {1, 2, 3, 4, 5}
print(B)  # {1, 2, 3, 4}  (permanece igual)

A = {1, 2, 3, 4}

# Removendo um elemento existente
A.discard(3)
print(A)   # {1, 2, 4}

# Tentando remover um elemento que não existe
A.discard(10)
print(A)   # {1, 2, 4}  (não dá erro, apenas ignora)


A = {1, 2, 3, 4, 5}

# Remove e retorna um elemento aleatório
x = A.pop()

print(x)   # Pode ser 1, 2, 3, 4 ou 5 (não é garantido qual)
print(A)   # Conjunto agora tem um elemento a menos


A = {1, 2, 3, 4}

# Removendo um elemento existente
A.remove(3)
print(A)   # {1, 2, 4}

# Tentando remover um elemento inexistente
A.remove(10)   # ❌ Gera erro: KeyError


# Em uma lista
lista = [10, 20, 30, 40]
print(len(lista))   # 4

# Em uma string
texto = "Python"
print(len(texto))   # 6

# Em um conjunto
conjunto = {1, 2, 3, 4, 5}
print(len(conjunto))   # 5

# Em um dicionário
dicionario = {"a": 1, "b": 2, "c": 3}
print(len(dicionario))   # 3


conjunto = {1, 2, 3}
print(3 in conjunto)   # True
print(5 in conjunto)   # False
