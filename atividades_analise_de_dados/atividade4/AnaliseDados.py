import pandas as pd

df = pd.read_csv("estoque_supermercado.csv")

df["preco"] = (
    df["preco"]
    .astype(str)
    .str.replace("R$", "", regex=False)
    .str.strip()
    .str.replace(",", ".", regex=False)
)

df["preco"] = pd.to_numeric(df["preco"], errors="coerce")

media_precos = df["preco"].mean()
df["preco"] = df["preco"].fillna(media_precos).astype(float)

df["quantidade"] = pd.to_numeric(
    df["quantidade"], errors="coerce"
)

df["quantidade"] = (
    df["quantidade"]
    .fillna(0)
    .astype(int)
)

df["setor"] = (
    df["setor"]
    .fillna("sem setor")
    .astype(str)
    .str.strip()
    .str.lower()
)

df["setor"] = df["setor"].replace("", "sem setor")

df["data_compra"] = pd.to_datetime(
    df["data_compra"],
    dayfirst=True,
    errors="coerce"
)

df["data_vencimento"] = pd.to_datetime(
    df["data_vencimento"],
    dayfirst=True,
    errors="coerce"
)

hoje = pd.Timestamp("2026-10-27")

print("\n--- BASE DE DADOS LIMPA ---")
print(df.head())

inicio_semana = pd.Timestamp("2026-10-27")
fim_semana = pd.Timestamp("2026-11-03")

vencendo_semana = df[
    df["data_vencimento"].between(
        inicio_semana, fim_semana
    )
].sort_values("data_vencimento")

print("\n--- PRODUTOS VENCENDO ESTA SEMANA ---")
print(vencendo_semana[
    ["nome", "quantidade", "setor", "data_vencimento"]
])

print("\n--- MAIOR QUANTIDADE A VENCER ---")

if not vencendo_semana.empty:
    maior_quantidade = vencendo_semana[
        "quantidade"
    ].max()

    produtos_maior_quantidade = vencendo_semana[
        vencendo_semana["quantidade"] == maior_quantidade
    ]

    print(produtos_maior_quantidade[
        ["nome", "quantidade", "data_vencimento"]
    ])
else:
    print("Nenhum produto vencendo no período.")

inicio_compras = pd.Timestamp("2026-10-24")

compras_recentes = df[
    df["data_compra"].between(inicio_compras, hoje)
].sort_values("data_compra")

print("\n--- COMPRAS RECENTES ---")
print(compras_recentes[
    ["nome", "quantidade", "data_compra"]
])

sem_vencimento = df[df["data_vencimento"].isna()]

print("\n--- PRODUTOS SEM VENCIMENTO ---")
print(sem_vencimento[
    ["nome", "quantidade", "setor"]
])

df["valor_total_estoque"] = (
    df["quantidade"] * df["preco"]
)

valor_por_setor = (
    df.groupby("setor")["valor_total_estoque"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- VALOR PATRIMONIAL POR SETOR ---")
print(valor_por_setor)

if not valor_por_setor.empty:
    print("\n--- SETOR COM MAIOR VALOR PATRIMONIAL ---")
    print(f"Setor: {valor_por_setor.idxmax()}")
    print(f"Valor: R$ {valor_por_setor.max():.2f}")
