
import json

with open("base1.json", "r", encoding="utf-8") as arquivo:
    dados1 = json.load(arquivo)

with open("base2.json", "r", encoding="utf-8") as arquivo:
    dados2 = json.load(arquivo)

with open("base3.json", "r", encoding="utf-8") as arquivo:
    dados3 = json.load(arquivo)


lista_aniversariantes = []

for funcionario in dados1:
    aniversariante = {
        "nome": funcionario["nome"],
        "aniversario": funcionario["aniversario"]
    }
    lista_aniversariantes.append(aniversariante)

for funcionario in dados2:
    aniversariante = {
        "nome": funcionario["nome"],
        "aniversario": funcionario["aniversario"]
    }
    lista_aniversariantes.append(aniversariante)

for funcionario in dados3:
    aniversariante = {
        "nome": funcionario["nome"],
        "aniversario": funcionario["aniversario"]
    }
    lista_aniversariantes.append(aniversariante)


with open("aniversariantes.json", "w", encoding="utf-8") as arquivo:
    json.dump(
        lista_aniversariantes,
        arquivo,
        indent=4,
        ensure_ascii=False
    )

print("Lista de aniversariantes consolidada com sucesso!")
