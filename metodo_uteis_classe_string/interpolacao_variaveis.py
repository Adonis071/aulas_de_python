""" Operador % 
- %s → string
- %d → inteiro
- %f → floa
"""
nome = "Adonis"
idade = 30
print("Meu nome é %s e tenho %d anos." % (nome, idade))


"""Método .format() Introduzido no Python 2.6/3.0, é mais flexível"""
nome = "Adonis"
idade = 30
print("Meu nome é {} e tenho {} anos.".format(nome, idade))

# Com índices
print("Meu nome é {0} e tenho {1} anos. {0} gosta de Python.".format(
    nome, idade))

# Com nomes
print("Meu nome é {n} e tenho {i} anos.".format(n=nome, i=idade))

"""f-strings (Python 3.6+)
A forma mais moderna e recomendada. Muito mais legível e poderosa.
"""

nome = "Adonis"
idade = 30
print(f"Meu nome é {nome} e tenho {idade} anos.")

# Pode incluir expressões
print(f"Daqui a 5 anos terei {idade + 5} anos.")
