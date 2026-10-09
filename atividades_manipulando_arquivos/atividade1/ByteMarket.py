print("=== Byte Market ===")

usuario = input("Digite seu nome para iniciar a compra: ")

produtos = []

total = 0.0

while True:
    produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")

    if produto.lower() == "fim":
        break

    preco = float(input("Digite o preço do produto: R$ "))

    produtos.append([produto, preco])

    total += preco

print("\n--- FINALIZANDO COMPRA ---")

with open("pagamento.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("===== RECIBO DE COMPRA =====\n")
    arquivo.write(f"Cliente: {usuario}\n\n")

    arquivo.write("Produtos:\n")

    for produto, preco in produtos:
        arquivo.write(f"{produto} - R$ {preco:.2f}\n")

    arquivo.write(f"\nTOTAL: R$ {total:.2f}\n")

print("Recibo salvo com sucesso em pagamento.txt")

print("\n--- PROCESSANDO PAGAMENTO ---")

with open("pagamento.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

posicao = texto.find("TOTAL:")

valor_total = texto[posicao + len("TOTAL:"):].strip()

print(f"Compra processada com sucesso! Valor cobrado: {valor_total}")
