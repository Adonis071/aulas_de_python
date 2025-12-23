lista = []

# Método de adicionar elementos na lista. (append())
lista.append(1)
lista.append('Python')
lista.append([10, 20, 50])
print(lista)
# Método cler() serve para limpar uma lista
lista.clear()
print(lista)

# Método copy() copia a lista existente, OBS: o método copy() não altera a lista original
lista = ['Água', 20, 'Mamão']
lista.copy()
print(lista)

# Método [].count() serve para contar quantas vezes um elemento aparece dentro de uma lista
cores = ['Vermelho', 'Azul', 'Verde', 'Azul']

print(cores.count('Azul'))
print(cores.count('Verde'))
print(cores.count('Vermelho'))

# Método [].extend() junta uma lista ao final de outra já existente, não elimina as duplicatas
linguagens = ['Python', 'C', 'Js']
print(linguagens)  # ['Python', 'C', 'Js']

linguagens.extend(['java', 'csharp', 'Js'])
print(linguagens)  # ['Python', 'C', 'Js', 'java', 'csharp']

# Método index() trás a primeira ocorr^ência do objeto dentro da lista
# OBS ele não retorna todas as ocorrências deste objeto , apenas uma vez.

linguagens = ['python', 'js', 'c', 'java', 'csharp', 'java']

print(linguagens.index('java'))  # saída 3
print(linguagens.index('csharp'))  # saida 4

# Método pop() remove o ultimo elemento da lista. se passarmos
# para remover um objeto especifico podemos passar o índice EX: .pop(1)

linguagens = ['python', 'js', 'c', 'java', 'csharp', 'java']
print(linguagens.pop())  # saída java
print(linguagens.pop())  # saída csharp
print(linguagens.pop(1))  # saida js
print(linguagens.pop(0))  # saída python

# Método remove() remove o elemento que passamos .
# OBS ele remove apenas na primeira ocorrência desse elemento
# se quisermos remover a quantidade específica de elementos que contém na lista
# devemospassas a quantidade de vezes que esse elemento se repete
# ou montar uma lógica .

linguagens = ['python', 'js', 'c', 'java', 'csharp', 'java']

linguagens.remove('java')
print(linguagens)

# O método reverse() é usado para fazer o espelhamento de lista

linguagens = ['python', 'js', 'c', 'java', 'csharp', 'java']
linguagens.reverse()

print(linguagens)  # saída ['java', 'csharp', 'java', 'c', 'js', 'python']

# O método sort() ordena em ordem alfabetica a lista
linguagens = ['python', 'js', 'c', 'java', 'csharp', 'java']
linguagens.sort()
print(linguagens)  # ['c', 'csharp', 'java', 'java', 'js', 'python']


# podemoa espelhar uma lista, igual fazemos com fatiamento de string
linguagens = ['python', 'js', 'c', 'java', 'csharp', 'java']
linguagens.sort(reverse=True)
print(linguagens)  # ['python', 'js', 'java', 'java', 'csharp', 'c']

# Ordenando da menor string para a maior
linguagens = ['python', 'js', 'c', 'java', 'csharp', 'java']
linguagens.sort(key=lambda x: len(x))
print(linguagens)  # ['c', 'js', 'java', 'java', 'python', 'csharp']

# podemos combinar os argumentos do método sort
# key+lambida e reverse+True ele organiza a lista pelo começando da maior palavra
# para a menor
linguagens = ['python', 'js', 'c', 'java', 'csharp', 'java']
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)  # ['python', 'csharp', 'java', 'java', 'js', 'c']

# O método len() tras o tamanho da lista
linguagens = ['python', 'js', 'c', 'java', 'csharp', 'java']
print(len(linguagens))  # 6

# Existe uma função chamada sorted é funciona como o metodo sort)
# porém é uma função

# Ordem alfabética
linguagens = ['python', 'js', 'c', 'java', 'csharp', 'java']
print(sorted(linguagens))  # ['c', 'csharp', 'java', 'java', 'js', 'python']


linguagens = ['python', 'js', 'c', 'java', 'csharp', 'java']
# ['c', 'js', 'java', 'java', 'python', 'csharp']
print(sorted(linguagens, key=lambda x: len(x)))

linguagens = ['python', 'js', 'c', 'java', 'csharp', 'java']
# ['python', 'csharp', 'java', 'java', 'js', 'c']
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
