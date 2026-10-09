import json

loja = {
    "nome": "TechStore",
    "produtos": [
        {
            "nome": "Teclado",
            "preco": 150.00,
            "quantidade": 10
        },
        {
            "nome": "Mouse",
            "preco": 80.00,
            "quantidade": 15
        },
        {
            "nome": "Monitor",
            "preco": 950.00,
            "quantidade": 5
        }
    ]
}

with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(loja, arquivo, indent=4, ensure_ascii=False)


with open("estoque.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)

for produto in dados_lidos["produtos"]:
    print(f"O produto {produto['nome']} custa R$ {produto['preco']:.2f}")


novo_produto = {
    "nome": "Fone de Ouvido",
    "preco": 120.00,
    "quantidade": 20
}

dados_lidos["produtos"].append(novo_produto)


with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_lidos, arquivo, indent=4, ensure_ascii=False)

print("\nNovo produto adicionado com sucesso!")
