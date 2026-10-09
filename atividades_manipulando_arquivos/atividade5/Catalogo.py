import json

catalogo_livros = []

with open("banco_livros.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(";")

        livro = {
            "id": int(dados[0]),
            "nome": dados[1],
            "descricao": dados[2],
            "preco": float(dados[3]),
            "em_estoque": int(dados[4])
        }

        catalogo_livros.append(livro)

livros_adicionais = [
    {
        "id": 31,
        "nome": "Clean Code",
        "descricao": "Educação com códigos",
        "preco": 150.00,
        "em_estoque": 10
    },
    {
        "id": 32,
        "nome": "Diário de um Banana",
        "descricao": "Livro de histórias",
        "preco": 15.00,
        "em_estoque": 50
    },
    {
        "id": 33,
        "nome": "O Hobbit",
        "descricao": "Uma aventura fantástica",
        "preco": 49.90,
        "em_estoque": 12
    },
    {
        "id": 34,
        "nome": "Dom Casmurro",
        "descricao": "Romance de Machado de Assis",
        "preco": 35.00,
        "em_estoque": 20
    },
    {
        "id": 35,
        "nome": "O Pequeno Príncipe",
        "descricao": "Uma história sobre amizade",
        "preco": 29.90,
        "em_estoque": 8
    }
]

catalogo_livros += livros_adicionais

with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)

with open("catalogo.json", "r", encoding="utf-8") as arquivo:
    dados_livros = json.load(arquivo)

    total_estoque = 0

    print("Livros com menos de 15 unidades em estoque:\n")

    for livro in dados_livros:
        if livro["em_estoque"] < 15:
            print(f'{livro["nome"]} - {livro["em_estoque"]} unidades')

        subtotal = livro["preco"] * livro["em_estoque"]
        total_estoque += subtotal

    print(f"\nValor total do estoque da livraria: R$ {total_estoque:.2f}")












































































