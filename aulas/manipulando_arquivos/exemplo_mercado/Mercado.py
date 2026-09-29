produtos = []

produtos.append("Arroz")
produtos.append("Alga")
produtos.append("Salmão")
produtos.append("Banana")
produtos.append("Açaí")
produtos.append("Iogurte")

# print(produtos[0])
# ESCRITA -> Write -> 'w'
# open -> Cria/Usa 'arquivo.txt'
# as -> cria variável arquivo, e atribui os valores do documento
# arquivo.txt à ela
with open("recibo.txt", "w", encoding='utf-8') as arquivo:
    for produto in produtos:
        arquivo.write(f"{produto}\n")

# LEITURA -> read -> 'r'
# open -> ler todos os textos escritos dentro do recibo.txt
with open("recibo.txt", "r", encoding='utf-8') as arquivo:
    texto = arquivo.read()

    posicao = texto.find("Banana")

    print(posicao)

    produto_vencido = texto[posicao:posicao+6]

    print(f"O produto {produto_vencido} está vencido")