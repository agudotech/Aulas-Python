
import pandas as pd

# 1. Ler o arquivo enviado pelo professor
df = pd.read_excel("dados_despadronizados.xlsx")

# Garantir que as colunas de texto possam ser tratadas com .str
df["cpf"] = df["cpf"].astype("string")
df["numero"] = df["numero"].astype("string")
df["salario"] = df["salario"].astype("string")

# 2. Formatar o CPF: remover pontos, traços e outros caracteres
df["cpf_formatado"] = df["cpf"].str.replace(r"\D", "", regex=True)

# 3. Validar o CPF: deve possuir exatamente 11 dígitos
df["cpf_valido"] = df["cpf_formatado"].str.fullmatch(r"\d{11}", na=False)

# 4. Formatar o número de telefone: manter somente os dígitos
df["numero_formatado"] = df["numero"].str.replace(r"\D", "", regex=True)

# 5. Validar o telefone: deve possuir de 10 a 13 dígitos
df["numero_valido"] = df["numero_formatado"].str.fullmatch(
    r"\d{10,13}", na=False
)

# 6. Formatar os salários
def formatar_salario(salario):
    salario = salario.strip()

    # Remover símbolos de moeda e espaços
    salario = pd.Series([salario]).str.replace(
        r"[^\d,.\-]", "", regex=True
    ).iloc[0]

    # Se houver vírgula, considerar a vírgula como separador decimal
    if "," in salario:
        salario = salario.replace(".", "")
        salario = salario.replace(",", ".")

    return salario


salarios = df["salario"].apply(formatar_salario)

df["salario_formatado"] = pd.to_numeric(
    salarios, errors="coerce"
)

# 7. Criar uma coluna com o salário anual
df["salario_anual"] = df["salario_formatado"] * 12

# 8. Selecionar as colunas solicitadas pelo professor
colunas = [
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

df_final = df[colunas]

# 9. Exibir os dados tratados
print("\n--- DADOS PADRONIZADOS ---\n")
print(df_final.to_string(index=False))

print("\n--- RESUMO DAS VALIDAÇÕES ---")
print("CPFs válidos:", df["cpf_valido"].sum())
print("CPFs inválidos:", (~df["cpf_valido"]).sum())
print("Telefones válidos:", df["numero_valido"].sum())
print("Telefones inválidos:", (~df["numero_valido"]).sum())

# 10. Salvar o resultado em CSV
df_final.to_csv(
    "dados_padronizados.csv",
    index=False,
    sep=";",
    encoding="utf-8-sig"
)

print("\nArquivo dados_padronizados.csv salvo com sucesso!")

