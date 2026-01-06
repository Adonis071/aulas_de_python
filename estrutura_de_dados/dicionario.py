# Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são
# únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves :{}
# e contém uma lista de pares chace:valor separados por vírgula

pessoa = {'nome': 'Adonis', 'idade': 50}


# usando a classe dict()
pessoa = dict(nome='Adonis', idade=50)

# Adicionando mais um elemento ao dicionário
pessoa['Telefone'] = '9187878970'

print(pessoa)  # {'nome': 'Adonis', 'idade': 50, 'Telefone': '9187878970'}

# acessando valores do nosso dicionário
print(pessoa['nome'])  # Adonis
print(pessoa['idade'])  # 50
print(pessoa['Telefone'])  # 9187878970

# Alterando os valores existente dento do meu dicionário (Sobrescrevendo)

pessoa['nome'] = 'Léo'
pessoa['idade'] = 70
pessoa['Telefone'] = 9197252222

print(pessoa)  # {'nome': 'Léo', 'idade': 70, 'Telefone': 9197252222}

# Dicionário aninhado

# Exemplo de dicionário aninhado obs podemos ter quantos dicionários aninhados quisermos
alunos = {
    "João": {
        "idade": 20,
        "curso": "Engenharia",
        "notas": {"Matemática": 8.5, "Física": 7.0, "Química": 9.0}
    },
    "Maria": {
        "idade": 22,
        "curso": "Medicina",
        "notas": {"Biologia": 9.5, "Química": 8.0, "Anatomia": 9.2}
    },
    "Pedro": {
        "idade": 19,
        "curso": "Direito",
        "notas": {"História": 7.8, "Sociologia": 8.3, "Filosofia": 7.5}
    }
}

# Acessando dados
print(alunos["João"]["curso"])          # Engenharia
print(alunos["Maria"]["notas"]["Biologia"])  # 9.5

# iterando no dicionário aninhado
alunos = {
    "João": {
        "idade": 20,
        "curso": "Engenharia",
        "notas": {"Matemática": 8.5, "Física": 7.0, "Química": 9.0}
    },
    "Maria": {
        "idade": 22,
        "curso": "Medicina",
        "notas": {"Biologia": 9.5, "Química": 8.0, "Anatomia": 9.2}
    },
    "Pedro": {
        "idade": 19,
        "curso": "Direito",
        "notas": {"História": 7.8, "Sociologia": 8.3, "Filosofia": 7.5}
    }
}

# Iterando sobre os valores
for nome, dados in alunos.items():
    print(f"Aluno: {nome}")
    for chave, valor in dados.items():
        if isinstance(valor, dict):  # se for outro dicionário (notas)
            print(f"  {chave}:")
            for materia, nota in valor.items():
                print(f"    {materia}: {nota}")
        else:
            print(f"  {chave}: {valor}")

""""SAÍDA
Aluno: João
  idade: 20
  curso: Engenharia
  notas:
    Matemática: 8.5
    Física: 7.0
    Química: 9.0
Aluno: Maria
  idade: 22
  curso: Medicina
  notas:
    Biologia: 9.5
    Química: 8.0
    Anatomia: 9.2
Aluno: Pedro
  idade: 19
  curso: Direito
  notas:
    História: 7.8
    Sociologia: 8.3
    Filosofia: 7.5


"""
