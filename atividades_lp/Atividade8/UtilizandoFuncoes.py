def aluno(nome, primeiro, segundo, terceiro, quarto):
    media = (primeiro + segundo + terceiro + quarto) / 4

    print("Nome:", nome)
    print("1º bimestre:", primeiro)
    print("2º bimestre:", segundo)
    print("3º bimestre:", terceiro)
    print("4º bimestre:", quarto)
    print("Média final:", media)

    if media >= 7:
        print("Aluno APROVADO!")
    else:
        print("Aluno REPROVADO!")


nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota do 1º bimestre: "))
n2 = float(input("Digite a primeira nota do 2º bimestre: "))
n3 = float(input("Digite a primeira nota do 3º bimestre: "))
n4 = float(input("Digite a primeira nota do 4º bimestre: "))

aluno(nome, n1, n2, n3, n4)

