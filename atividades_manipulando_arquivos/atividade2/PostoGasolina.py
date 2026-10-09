from Combustivel import Combustivel
from Veiculo import Veiculo
from Abastecimento import Abastecimento

etanol = Combustivel("Etanol")
gasolina = Combustivel("Gasolina")
diesel = Combustivel("Diesel")

carro = Veiculo("Carro", "ABC-1234")
moto = Veiculo("Moto", "DEF-5678")
van = Veiculo("Van Escolar", "GHI-9012")
limosine = Veiculo("Limosine", "ABC-0001")
onibus = Veiculo("Onibus", "ABC-0002")

caminhao = Veiculo("Caminhao", "DEF-0003")
picape = Veiculo("Picape", "DEF-0004")
trator = Veiculo("Trator", "DEF-0005")
ambulancia = Veiculo("Ambulancia", "DEF-0006")
taxi = Veiculo("Taxi", "DEF-0007")

abastecimento1 = Abastecimento(carro, etanol, 50)
abastecimento2 = Abastecimento(moto, gasolina, 25)
abastecimento3 = Abastecimento(van, diesel, 200)
abastecimento4 = Abastecimento(limosine, gasolina, 400)
abastecimento5 = Abastecimento(onibus, diesel, 600)
abastecimento6 = Abastecimento(carro, gasolina, 150)

abastecimento7 = Abastecimento(caminhao, diesel, 350)
abastecimento8 = Abastecimento(picape, gasolina, 120)
abastecimento9 = Abastecimento(trator, diesel, 500)
abastecimento10 = Abastecimento(ambulancia, gasolina, 80)
abastecimento11 = Abastecimento(taxi, etanol, 70)

abastecimentos = [
    abastecimento1,
    abastecimento2,
    abastecimento3,
    abastecimento4,
    abastecimento5,
    abastecimento6,
    abastecimento7,
    abastecimento8,
    abastecimento9,
    abastecimento10,
    abastecimento11
]

total_etanol = 0
total_gasolina = 0
total_diesel = 0

for abastecimento in abastecimentos:
    if abastecimento.combustivel.nome == "Etanol":
        total_etanol += abastecimento.valor
    elif abastecimento.combustivel.nome == "Gasolina":
        total_gasolina += abastecimento.valor
    elif abastecimento.combustivel.nome == "Diesel":
        total_diesel += abastecimento.valor

total_dia = total_etanol + total_gasolina + total_diesel

with open("recibo_posto.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("========== POSTO DE GASOLINA ==========\n")

    for abastecimento in abastecimentos:
        arquivo.write(
            f"{abastecimento.veiculo}\n"
            f"Combustível: {abastecimento.combustivel.nome}\n"
            f"Valor: R$ {abastecimento.valor:.2f}\n\n"
        )

    arquivo.write("========================================\n")
    arquivo.write(f"Etanol: R$ {total_etanol:.2f}\n")
    arquivo.write(f"Gasolina: R$ {total_gasolina:.2f}\n")
    arquivo.write(f"Diesel: R$ {total_diesel:.2f}\n")
    arquivo.write(f"TOTAL DO DIA: R$ {total_dia:.2f}\n")

with open("recibo_posto.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

print(texto)

print("========== RESUMO DAS VENDAS ==========")

for linha in texto.splitlines():
    if linha.startswith(("Etanol:", "Gasolina:", "Diesel:", "TOTAL DO DIA:")):
        print(linha)