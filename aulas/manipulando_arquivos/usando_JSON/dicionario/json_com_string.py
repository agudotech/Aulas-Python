# IMPORTANDO BIBLIOTECA
# import -> nome da biblioteca
# como a biblioteca json é nativa do Python, nós não precisamos instalar
import json

dados_dicionario = {
    "produto": "Frango"
    "preco": 25.00,
    "em_estoque": True
}

# json_string = json.dumps(dados_dicionario, ensure_ascii=False , indent=1)
# print(json_string)
#
# texto_json = '{"produto": "carne", "preco": 50.00, "em_estoque": true}'
#
# novo_dicionario = json.loads(texto_json)
# print(novo_dicionario["produto"])

with open('json_file.json', 'w', encoding='utf-8') as arquivo:


