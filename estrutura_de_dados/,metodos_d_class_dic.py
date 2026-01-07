alunos = {
    "idade": 20,
    "curso": "Engenharia",
    "notas": {"Matemática": 8.5, "Física": 7.0, "Química": 9.0}
}

alunos.clear()
print(alunos)  # {}

alunos = {
    "idade": 20,
    "curso": "Engenharia",
    "notas": {"Matemática": 8.5, "Física": 7.0, "Química": 9.0}
}

# Apagar uma chave de nível superior
del alunos["idade"]
print(alunos)
# {'curso': 'Engenharia', 'notas': {'Matemática': 8.5, 'Física': 7.0, 'Química': 9.0}}

# Apagar uma chave dentro do dicionário aninhado
del alunos["notas"]["Física"]
print(alunos)
# {'curso': 'Engenharia', 'notas': {'Matemática': 8.5, 'Química': 9.0}}

# Apagar o dicionário aninhado inteiro
del alunos["notas"]
print(alunos)
# {'curso': 'Engenharia'}

# Apagar a variável (remove o dicionário inteiro da memória/referência)
del alunos
# print(alunos)  # NameError: name 'alunos' is not defined

alunos = {
    "idade": 20,
    "curso": "Engenharia",
    "notas": {"Matemática": 8.5, "Física": 7.0, "Química": 9.0}
}

# {'idade': 20, 'curso': 'Engenharia', 'notas': {'Matemática': 8.5, 'Física': 7.0, 'Química': 9.0}}
copia = alunos.copy()
# Alterando o valor da chave idade para 29
copia["idade"] = 29

# Ajustando as notas do dicionário da chave nota dentro do meu dict alunos
copia["notas"] = {"Matemática": 8.5,
                  # {'idade': 29, 'curso': 'Engenharia', 'notas': {'Matemática': 8.5, 'Física': 7.0, 'Química': 9.0, 'Geografia': 9}}
                  "Física": 7.0, "Química": 9.0, "Geografia": 9}

# O método copy pode ser usado para salvar uma cópia do
# dicionário que estamos trabalhando, com isso podemos manipular a cópia sem alterar a estrutura do dicionário orignal

# 1. keys() → retorna as chaves
print(alunos.keys())
# Saída: dict_keys(['idade', 'curso', 'notas'])

# 2. values() → retorna os valores
print(alunos.values())
# Saída: dict_values([20, 'Engenharia', {'Matemática': 8.5, 'Física': 7.0, 'Química': 9.0}])

# 3. items() → retorna pares (chave, valor)
print(alunos.items())
# Saída: dict_items([('idade', 20), ('curso', 'Engenharia'), ('notas', {...})])

# 4. get() → acessa valor de forma segura
print(alunos.get("curso"))  # None caso não encontre curso
# Saída: Engenharia
print(alunos.get("nome", "Não encontrado"))
# Saída: Não encontrado

# 5. update() → adiciona ou altera valores
alunos.update({"nome": "João"})
print(alunos)
# Saída: {'idade': 20, 'curso': 'Engenharia', 'notas': {...}, 'nome': 'João'}

# 6. pop() → remove uma chave específica
# OBS se o método pop nap achar "idade" lançará uma excessão podemos passar um argumento a mais para conter isso

alunos.pop("idade", "não encontrado")
print(alunos)
# Saída: {'curso': 'Engenharia', 'notas': {...}, 'nome': 'João'}

# 7. popitem() → remove o último item inserido na sequencia
alunos.popitem()
print(alunos)
# Saída: {'curso': 'Engenharia', 'notas': {...}}

# 8. setdefault() → retorna valor da chave ou cria se não existir se existe um valos na chave ele
# respeita e não altera em nada
alunos.setdefault("cidade", "Belém")
print(alunos)
# Saída: {'curso': 'Engenharia', 'notas': {...}, 'cidade': 'Belém'}

# 9. fromkeys() → cria novo dicionário com chaves de uma lista
novo = dict.fromkeys(["a", "b", "c"], 0)
print(novo)
# Saída: {'a': 0, 'b': 0, 'c': 0}


alunos = {
    "idade": 20,
    "curso": "Engenharia",
    "notas": {"Matemática": 8.5, "Física": 7.0, "Química": 9.0}
}

# Checar chaves (padrão: verifica apenas chaves)
print("idade" in alunos)          # True
print("nome" in alunos)           # False
print("Engenharia" in alunos)     # False (não procura em valores)

# Checar valores
print("Engenharia" in alunos.values())  # True
print(20 in alunos.values())            # True

# Checar pares (chave, valor)
print(("curso", "Engenharia") in alunos.items())  # True
print(("idade", 30) in alunos.items())            # False

# Negação
print("nome" not in alunos)           # True

# Checar chave dentro do dicionário aninhado
print("Matemática" in alunos["notas"])          # True
print(8.5 in alunos["notas"].values())          # True
