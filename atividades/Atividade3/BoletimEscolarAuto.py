nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
frequencia_digitada = int(input("Digite sua frequencia: "))
media = (nota1 + nota2) / 2
porcentagem_frequencia_min = (200 * 75) / 100

frequencia_do_aluno = (frequencia_digitada * 100) / 200

if frequencia_do_aluno >=  75 and media >= 7.0:
    print(f"A média do aluno foi: {media:.2f}. ""\nEle foi aprovado:", aprovado)


