print("✦ Bem-vindo(a) ao Formulário de Elegibilidade ✦ ")
print()
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
saude = bool(input("Você tem plano de saúde? "))
print()
 
aceito = idade >= 18 and idade < 60 and saude 

print("Seu nome é", nome, "\nsua idade é:", idade, "\nVocê foi aceito?", aceito)