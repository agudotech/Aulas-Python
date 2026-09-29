from atividades_lp.Atividade3.CalculadoraDeLucroDaEmpresa import nome_produto

usuario =  input("Digite seu nome para iniciar a compra: ")

produtos = []

print("\nDigite os produtos (digite 'fim' no nome do produto para encerrar)\n")

while True:
    nome_produto = input("Digite o nome do produto: ")

    if nome_produto.strip() .lower(