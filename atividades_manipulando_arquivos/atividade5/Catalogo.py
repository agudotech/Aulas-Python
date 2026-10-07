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
























































































