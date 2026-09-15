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


