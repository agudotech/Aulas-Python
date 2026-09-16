orcamento_da_viagem = 500

while orcamento_da_viagem > 0:

    gasto_da_vez = float(input("Digite o valor do gasto: "))

    orcamento_da_viagem -= gasto_da_vez

    print(f"Saldo restante: R$ {orcamento_da_viagem:.2f}")

print("Atenção: Você ficou sem saldo ou estourou seu orçamento!")
