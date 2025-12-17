# estruturas de decisão

''' saldo = 2000
saque = float(input("Informa o valor do saque: ?\n"))


if saldo >= saque:
    print(f'Saque realizado.')

if saldo < saque:
    print(f'Saldo insuficiente!. Seu Saldo é de {saldo}')
'''
# Outro exemplo de if elif e if else estruturas de decisões:

# estruturas de decisão

''' saldo = 2000
opcao = float(input("Escolha uma das opções: ?\nSAcar: [1]\nExtrato: [2]\n"))


if opcao == 1:
    print(f'Saque realizado.')

elif opcao == 2:
    print(f'Seu extrato {saldo}')

else:
    print(f'Opção inválida.')
'''
# Estruturas condicionais aniinhadas

'''conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 2001
cheque_especial = 290

if conta_normal:
    if saldo >= saque:
        print(f'Saque realizado.')
    elif saque <= (saldo + cheque_especial):
        print(f'Saque realizado com limite do ceque especial.')
    else:
        print(f'Não foi possivel realizar a operação.')
elif conta_universitaria:
    if saldo >= saque:
        print(f'Saque realizado com sucesso.')
    else:
        print(f'saldo insuficiente.')
'''

# if Ternário
saldo = 10
saque = 50
status = 'Sucesso' if saldo >= saque else 'Falha'
print(f'status: {status}ao realizar a operação')
