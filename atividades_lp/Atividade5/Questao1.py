# MENU DA LANCHONETE

codigo = int(input("Digite o código do produto (1 a 4): "))

if codigo == 1:
    print("Cachorro-quente - R$ 10,00")
elif codigo == 2:
    print("Hambúrguer - R$ 15,00")
elif codigo == 3:
    print("Batata Frita - R$ 8,00")
elif codigo == 4:
    print("Refrigerante - R$ 5,00")
else:
    print("Código inválido")
