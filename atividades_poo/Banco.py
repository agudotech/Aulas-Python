print("Bem-vindo(a) ao NuRoxinho!\n")
class Banco:

    def __init__(self, titular, numero_conta, saldo, limite, tipo_conta):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.limite = limite
        self.tipo_conta = tipo_conta

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente")

    def mostrar_dados(self):
        print(f"Titular: {self.titular}")
        print(f"Conta: {self.numero_conta}")
        print(f"Saldo: R${self.saldo}")
        print(f"Limite: R${self.limite}")
        print(f"Tipo de conta: {self.tipo_conta}")
        print("-" * 35)


conta1 = Banco("Antonio", "1001", 1500.00,2500.00, "Conta Digital")
conta2 = Banco("Hugo", "1002", 1800.00, 6000.00, "Conta Digital")
conta3 = Banco("Lucas", "1003", 500.00, 400.00, "Conta Digital")
conta4 = Banco("Anastacia", "1004", 2500.00, 200.00, "Conta Digital")
conta5 = Banco("Luiza", "1005", 800.00, 1000.00, "Conta Digital")

contas = [conta1, conta2, conta3, conta4, conta5]

for conta in contas:
    conta.mostrar_dados()