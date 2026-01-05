# Entendendo o funcionamento da estrutura de dados set
# Um set é uma coleção que não possue objetos repetidos,
# usamos set para representar conjuntos matemáticosou eliminar itens duplicados de um iterável

primeiro_exemplo = set([1, 2, 9, 2, 1, 8])
print(primeiro_exemplo)  # {8, 1, 2, 9}

segundo_exemplo = set("abacaxi")
print(segundo_exemplo)  # {'x', 'a', 'c', 'i', 'b'}

terceiro_exemplo = set(("palio", "gol", "ford", "palio"))
print(terceiro_exemplo)  # {'gol', 'ford', 'palio'}

# OBS: Importante lembrar que o set não garante a ordem dos elementos do iterável
# Outa maneira de se criar um conjunto está no exemplo abaixo.

times_futebol = {"palmeiras", "clube do remo", "vasco", "palmeiras"}
print(times_futebol)  # {'vasco', 'clube do remo', 'palmeiras'}

# Podemos observar que a ordem foi alterada ou seja não podemos confiar no conjunto para garantir a ordem
# _________________________________________________________________________________________________________
# Acessando os dados
# Conjunto em python não suportam indexação e nem fatiamento
# caso queira acessar seus valores temos que converter o conjunto em lista ou usar um laço for.

numeross = {1, 2, 5, 1, 10, 11}
for num in numeross:
    print(num)  # 1 2 5 10 11

for ind, num in enumerate(numeross):
    print(f'{ind}: {num}')  # 0: 1 1: 2 2: 5 3: 10 4: 11

# [1, 2, 5, 10, 11] set convertido em lista já com os valores duplicadosk removidos
numeross = list(numeross)
print(numeross)
