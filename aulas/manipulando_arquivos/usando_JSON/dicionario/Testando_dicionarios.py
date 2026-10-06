#      index      0         1        2
lista_nomes =  ['João', 'Bianca', 'Italo']
tupla_nomes =  ['João', 'Bianca', 'Italo']

#    chave :  valor
dicionario_nomes = {
    "nome1" : "Maria",
    "nome2" : "Jose",
    "nome3" : "Bruno",
}

# print(lista_nomes)
# print(dicionario_nomes)
#
# print(dicionario_nomes["nome1"])
# print(dicionario_nomes["nome2"])
# print(dicionario_nomes["nome3"])

dicionario_ing_por = {
    'hi': 'Olá',
    'bye': 'Tchau'
}

pesquisa = input("Digite a palacra que quer traduzir:\nInglês")

if pesquisa in dicionario_ing_por:
    print(f"{dicionario_ing_por[pesquisa]}")
else:
    print("palavra não encontrada")
    
