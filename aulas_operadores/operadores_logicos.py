saldo = 1000
saque = 200
limite = 100
conta_especial = True

print(saldo >= saque and saque <= limite or saldo >= saque and saque >= limite)
print(not (saldo >= saque or saque <= limite))
print(conta_especial)
print(True and True)
print(False and True)
print(True and False)
print(True or True or True)
print(False or False or True)
print(False or False or False)
