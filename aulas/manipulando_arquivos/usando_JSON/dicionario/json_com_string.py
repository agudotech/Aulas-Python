# IMPORTANDO BIBLIOTECA, PACOTE, MÓDULO
# import -> nome da biblioteca
# como a biblioteca json é nativa do Python, nós não precisamos intalar ela no projeto
import json

dados_dicionario = {
    'produto': 'frango',
    'preco': 20.00,
    'em_estoque': True
}

json_string = json.dumps(dados_dicionario, ensure_ascii=False, indent=1)
print(json_string)

texto_json = f'{json_string}'
novo_dicionario = json.loads(texto_json)

print(novo_dicionario)