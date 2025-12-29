# Métodos de tuplas em Python

tupla = (10, 20, 20, 30, 40, 20)

# count() -> conta quantas vezes um elemento aparece
print(tupla.count(20))   # Saída: 3

# index() -> retorna o índice da primeira ocorrência do elemento
print(tupla.index(30))   # Saída: 3
print(tupla.index(20))   # Saída: 1
print(tupla.index(20, 2))  # Saída: 5

# Funções úteis aplicáveis a tuplas
print(len(tupla))        # 6 -> quantidade de elementos
print(max(tupla))        # 40 -> maior valor
print(min(tupla))        # 10 -> menor valor
print(sum(tupla))        # 140 -> soma dos valores
print(sorted(tupla))     # [10, 20, 20, 20, 30, 40] -> lista ordenada
