print("================================")
print("      GERADOR DE TABUADA")
print("================================")

numero = int(input("Digite um número para descobrir a tabuada: "))

contador = 1

print(f"\n Tabuada do {numero} \n")

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1

print("\n Tabuada finalizada!")
