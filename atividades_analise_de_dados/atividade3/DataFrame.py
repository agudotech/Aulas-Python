import pandas as pd

df = pd.read_csv(
    "dados_despadronizados.csv",
    dtype=str,
    encoding="utf-8-sig"
)

print("\n========== DADOS ORIGINAIS ==========")
print(df.to_string(index=False))

df["cpf"] = df["cpf"].str.replace(r"\D", "", regex=True)

def formatar_cpf(cpf):
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf

def validar_cpf(cpf):
    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    numeros = [int(digito) for digito in cpf]

    soma = sum(numeros[i] * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    if digito1 != numeros[9]:
        return False

    soma = sum(numeros[i] * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    return digito2 == numeros[10]

df["cpf_formatado"] = df["cpf"].apply(formatar_cpf)
df["cpf_valido"] = df["cpf"].apply(validar_cpf)

df["numero"] = df["numero"].str.replace(r"\D", "", regex=True)

def limpar_numero(numero):
    if len(numero) in (12, 13) and numero.startswith("55"):
        return numero[2:]
    return numero

df["numero"] = df["numero"].apply(limpar_numero)

def formatar_numero(numero):
    if len(numero) == 11:
        return f"({numero[:2]}) {numero[2:7]}-{numero[7:]}"
    elif len(numero) == 10:
        return f"({numero[:2]}) {numero[2:6]}-{numero[6:]}"
    return numero

def validar_numero(numero):
    return len(numero) in (10, 11)


df["numero_formatado"] = df["numero"].apply(formatar_numero)
df["numero_valido"] = df["numero"].apply(validar_numero)

def converter_salario(salario):
    salario = salario.strip()

    salario = salario.replace("R$", "").strip()

    if "," in salario:
        salario = salario.replace(".", "")
        salario = salario.replace(",", ".")

    return float(salario)

df["salario"] = df["salario"].apply(converter_salario)

def formatar_salario(salario):
    valor = f"{salario:,.2f}"
    valor = valor.replace(",", "X")
    valor = valor.replace(".", ",")
    valor = valor.replace("X", ".")
    return f"R$ {valor}"

df["salario_formatado"] = df["salario"].apply(formatar_salario)

df["salario_anual"] = df["salario"] * 12

df["salario_anual_formatado"] = df["salario_anual"].apply(
    formatar_salario
)

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
    "salario_anual",
    "salario_anual_formatado"
]

df = df[colunas]

print("\n========== DADOS PADRONIZADOS ==========")
print(df.to_string(index=False))

print("\n========== TIPOS DE DADOS ==========")
print(df.dtypes)

print("\n========== RESUMO DAS VALIDAÇÕES ==========")
print(f"Total de funcionários: {len(df)}")
print(f"CPFs válidos: {df['cpf_valido'].sum()}")
print(f"CPFs inválidos: {(~df['cpf_valido']).sum()}")
print(f"Números válidos: {df['numero_valido'].sum()}")
print(f"Números inválidos: {(~df['numero_valido']).sum()}")

df.to_csv(
    "dados_padronizados.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig"
)
print("\nArquivo dados_padronizados.csv salvo com sucesso!")
