# IF e ELSE -> SE e SENÃO

#CASE SENSITIVE -> E != e

idade = int(input("Digite sua idade: "))

# criando uma condição na execulçao do código
if idade >= 18: # executa SE a resposta boleana for True
    if idade > 65:
        print("Desculpa senhor, voce nao pode entrar nessa balada.")
    else:
        print("Voce pode entrar nessa balada.")
elif idade < 5:
        print("Alem de não entrar, voce nao pode entrar sozinho.")
else:
    print("Voce nao pode entrar, e menor de idade.")


nome = input("Digite seu nome: ")

if nome == "":
    print("Por favor, digite um nome válido: ")
else:
    print("Olá "+ nome +"! Seja bem-vindo(a) a nossa balada.")

