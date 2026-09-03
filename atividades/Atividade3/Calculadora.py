print("Bem-vindo(a) a Calculadora!")
print()
conta = float(input("Valor total da conta: "))
pessoas = int(input("Quantidade de pessoas: "))
print()
valor = float (conta / pessoas)
print('O valor total foi de R$', conta,', e cada pessoa deve pagar R$', round(valor,2))



