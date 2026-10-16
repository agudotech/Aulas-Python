import requests
import json

link_funcionarios = "http://192.168.205.100:8080/funcionarios"

resposta = requests.get(link_funcionarios)
resposta.raise_for_status()

lista_funcionarios = resposta.json()

def campo_vazio(valor):
    return valor is None or valor == ""

def consultar_cep(cep):
    cep = "".join(caractere for caractere in str(cep) if caractere.isdigit())

    if len(cep) != 8:
        return None

    try:
        link_cep = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(link_cep, timeout=10)

        if resposta.status_code != 200:
            return None

        dados_cep = resposta.json()

        if dados_cep.get("erro"):
            return None

        if not dados_cep.get("localidade") or not dados_cep.get("uf"):
            return None

        return dados_cep

    except requests.RequestException:
        return None

for funcionario in lista_funcionarios:
    print(f"\nFuncionário: {funcionario.get('nome', 'Sem nome')}")

    if campo_vazio(funcionario.get("cep")):
        while True:
            cep_digitado = input("Digite um CEP válido: ")
            dados_cep = consultar_cep(cep_digitado)

            if dados_cep is not None:
                funcionario["cep"] = dados_cep["cep"]
                break

            print("CEP inválido ou não encontrado. Tente novamente.")

    dados_cep = consultar_cep(funcionario["cep"])

    if dados_cep is not None:
        if campo_vazio(funcionario.get("cidade")):
            funcionario["cidade"] = dados_cep["localidade"]

        if campo_vazio(funcionario.get("estado")):
            funcionario["estado"] = dados_cep["uf"]

        if campo_vazio(funcionario.get("logradouro")):
            funcionario["logradouro"] = dados_cep.get("logradouro", "")

        if campo_vazio(funcionario.get("bairro")):
            funcionario["bairro"] = dados_cep.get("bairro", "")

with open(
    "dados_funcionarios_atualizados.json",
    "w",
    encoding="utf-8"
) as arquivo:
    json.dump(
        lista_funcionarios,
        arquivo,
        ensure_ascii=False,
        indent=4
    )

print("\nDados atualizados com sucesso!")
print("Arquivo salvo: dados_funcionarios_atualizados.json")
