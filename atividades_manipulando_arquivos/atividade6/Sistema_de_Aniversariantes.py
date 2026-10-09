import json

with open("base1.json", 'r') as arquivo:
    dados1 = json.load(arquivo)

with open("base2.json", 'r') as arquivo:
    dados2 = json.load(arquivo)

with open("base3.json", 'r') as arquivo:
    dados3 = json.load(arquivo)

lista_aniversariantes = []

for aniversariante in dados1:
    dicionario_aniversariante = {
        "nome": aniversariante['nome'],
        "aniversario": aniversariante['aniversario']
    }
    lista_aniversariantes.append(dicionario_aniversariante)

for aniversariante in dados2:
    dicionario_aniversariante = {
        "nome": aniversariante['nome'],
        "aniversario": aniversariante['aniversario']
    }
    lista_aniversariantes.append(dicionario_aniversariante)

for aniversariante in dados3:
    dicionario_aniversariante = {
        "nome": aniversariante['nome'],
        "aniversario": aniversariante['aniversario']
    }
    lista_aniversariantes.append(dicionario_aniversariante)

with open("aniversariantes.json", 'w') as arquivo:
    json.dump(lista_aniversariantes, arquivo, indent=4, ensure_ascii=False)

lista_aniversariantes.sort(key=lambda aniversariante: aniversariante['nome'])

with open("aniversariantes.json", 'w') as arquivo:
    json.dump(lista_aniversariantes, arquivo, indent=4, ensure_ascii=False)