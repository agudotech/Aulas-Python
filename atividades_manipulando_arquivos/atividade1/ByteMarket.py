# Sistema de Carrinho de Compras e Pagamento

# 1. Solicitando nome do usuário
usuario = input("Digite seu nome para iniciar a compra: ")

# Lista para armazenar os produtos e preços
produtos = []

# Variável para armazenar o valor total
total = 0.0

# 2. Loop de inserção de produtos no carrinho
while True:
    produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")

    # Condição de parada
    if produto.lower() == "fim":
        break

    preco = float(input("Digite o preço do produto: R$ "))

    # Adiciona o produto e o preço na lista
    produtos.append([produto, preco])

    # Soma o preço ao total
    total += preco

# 3. Geração do arquivo pagamento.txt
print("\n--- FINALIZANDO COMPRA ---")

with open("pagamento.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("===== RECIBO DE COMPRA =====\n")
    arquivo.write(f"Cliente: {usuario}\n\n")

    arquivo.write("Produtos:\n")

    for produto, preco in produtos:
        arquivo.write(f"{produto} - R$ {preco:.2f}\n")

    arquivo.write(f"\nTOTAL: R$ {total:.2f}\n")

print("Recibo salvo com sucesso em pagamento.txt")

# 4. Leitura e exibição final de pagamento
print("\n--- PROCESSANDO PAGAMENTO ---")

with open("pagamento.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

# Procura onde está escrito "TOTAL:"
posicao = texto.find("TOTAL:")

# Extrai o valor que vem depois de "TOTAL:"
valor_total = texto[posicao + len("TOTAL:"):].strip()

print(f"Compra processada com sucesso! Valor cobrado: {valor_total}")
