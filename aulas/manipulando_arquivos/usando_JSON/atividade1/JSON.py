import requests
import json
import os

arquivo_historico = "historico_pesquisa.json"

if os.path.exists(arquivo_historico):
    with open(arquivo_historico, "r", encoding="utf-8") as arquivo:
        try:
            historico = json.load(arquivo)
        except json.JSONDecodeError:
            historico = []
else:
    historico = []

cep = input("Digite o CEP (somente números): ")

cep = "".join(caractere for caractere in cep if caractere.isdigit())

if len(cep) != 8:
    print("CEP inválido! Digite um CEP com 8 números.")

else:
    try:
        link = f"https://viacep.com.br/ws/{cep}/json/"

        resposta = requests.get(link, timeout=10)

        resposta.raise_for_status()

        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado!")

        else:
            # Exibe os dados do endereço
            print("\n--- ENDEREÇO ENCONTRADO ---")
            print(f"CEP: {dados.get('cep')}")
            print(f"Logradouro: {dados.get('logradouro')}")
            print(f"Bairro: {dados.get('bairro')}")
            print(f"Cidade: {dados.get('localidade')}")
            print(f"Estado: {dados.get('uf')}")

            pesquisa = {
                "cep": dados.get("cep"),
                "logradouro": dados.get("logradouro"),
                "bairro": dados.get("bairro"),
                "cidade": dados.get("localidade"),
                "estado": dados.get("uf")
            }

            historico.append(pesquisa)

            with open(arquivo_historico, "w", encoding="utf-8") as arquivo:
                json.dump(historico, arquivo, indent=4, ensure_ascii=False)

            print("\nPesquisa salva no histórico com sucesso!")

    except requests.exceptions.Timeout:
        print("A consulta demorou demais. Tente novamente.")

    except requests.exceptions.ConnectionError:
        print("Erro de conexão! Verifique sua internet.")

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao consultar a API: {erro}")

    except (OSError, json.JSONDecodeError) as erro:
        print(f"Erro ao acessar o arquivo: {erro}")
