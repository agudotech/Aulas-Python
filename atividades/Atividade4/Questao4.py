saldo = float(input("Digite o saldo atual: R$ "))
saque = float(input("Digite o valor que deseja sacar: R$ "))

if saque <= saldo:
    saldo = saldo - saque
    print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
else:
    print("Saldo insuficiente para realizar esta operação.")
