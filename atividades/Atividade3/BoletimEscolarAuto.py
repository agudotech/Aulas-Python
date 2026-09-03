nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
frequencia = int(input("Digite sua frequencia: "))
media = (nota1 + nota2) / 2
print()
aprovado = (media >= 6.0) and (frequencia >= 75)
print(f"Sua media foi: {media}")
print(f"Aprovado: {aprovado}")



