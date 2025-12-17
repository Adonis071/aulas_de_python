"""intaxe Básica: texto[início:fim:passo]
Ínicio -> índice onde começa(inclusivo)
Fim -> índice onde termina (exclusivo)
Passo -> de quanros em quantos caracteres avançar
"""
frase = "Python é incrível"

print(frase[0:6])   # "Python"
print(frase[7:])    # "é incrível" (do índice 7 até o fim)
print(frase[:6])    # "Python" (do início até índice 6-1)

"""Ínices negativos contam a partir do fim da string"""

print(frase[-8:])   # "incrível"
print(frase[:-9])   # "Python é"
"""Usando passo"""

print(frase[::2])   # "Pto éncrvl" (pega de 2 em 2)
print(frase[::-1])  # "levícni é nohtyP" (string invertida)

"""
Expressão       | Resultado       | Explicação
----------------|-----------------|-------------------------------------
frase[0:6]      | "Python"        | Do índice 0 até 5
frase[7:]       | "é incrível"    | Do índice 7 até o fim
frase[:6]       | "Python"        | Do início até índice 5
frase[-8:]      | "incrível"      | Últimos 8 caracteres
frase[::-1]     | "levícni é nohtyP" | String invertida 
"""
