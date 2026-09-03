print("Bem-vindo ao Parque!")
print()
altura =  float(input("Digite a sua altura: "))
aceito = altura >= 1.40
bloqueado = altura < 1.40
print("✦ Você pode se divertir ✦ ", aceito)
print("Você não pode entrar na montanha-russa :( ", bloqueado)