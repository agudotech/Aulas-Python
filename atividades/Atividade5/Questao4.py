# ESTAÇÕES DO ANO

mes = int(input("Digite o número do mês (1 a 12): "))

if mes == 12 or mes == 1 or mes == 2:
    print("Verão")
elif mes == 3 or mes == 4 or mes == 5:
    print("Outono")
elif mes == 6 or mes == 7 or mes == 8:
    print("Inverno")
elif mes == 9 or mes == 10 or mes == 11:
    print("Primavera")
else:
    print("Mês inválido!")
