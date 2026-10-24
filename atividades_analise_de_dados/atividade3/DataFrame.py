import pandas as pd

dados = pd.read_csv(
    "dados_despadronizados.csv",
    dtype={
        "cpf": "string",
        "numero": "string",
        "salario": "string"
    }
)

dados["cpf_formatado"] = (
    dados["cpf"]
    .str.replace(r"\D", "", regex=True)
)

dados["cpf_valido"] = (
    dados["cpf_formatado"].str.fullmatch(r"\d{11}")
)

dados["numero_formatado"] = (
    dados["numero"]
    .str.replace(r"\D", "", regex=True)
)

dados["numero_valido"] = (
    dados["numero_formatado"].str.fullmatch(r"\d{10,11}")
)

salario_limpo = (
    dados["salario"]
    .str.replace(r"[^\d,.\-]", "", regex=True)
    .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
    .str.replace(",", ".", regex=False)
)

dados["salario_formatado"] = pd.to_numeric(
    salario_limpo,
    errors="coerce"
)

dados["salario_anual"] = dados["salario_formatado"] * 12

dados_padronizados = dados[
    [
        "nome",
        "cpf",
        "cpf_formatado",
        "cpf_valido",
        "numero",
        "numero_formatado",
        "numero_valido",
        "salario",
        "salario_formatado",
        "salario_anual"
    ]
]

dados_padronizados.to_csv(
    "dados_padronizados.csv",
    index=False,
    encoding="utf-8-sig"
)

print(dados_padronizados.to_string(index=False))

print("\nArquivo dados_padronizados.csv criado com sucesso!")
