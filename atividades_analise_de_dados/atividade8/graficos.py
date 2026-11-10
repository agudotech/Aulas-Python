import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customers-10000.csv")
print("Linhas e colunas:", df.shape)

paises = df["Country"].value_counts()
cidades = df["City"].value_counts()

print("\nPaís com mais clientes:", paises.index[0], "-", paises.iloc[0], "clientes")
print("\nCidades com mais clientes (há empate):")
print(cidades[cidades == cidades.max()])

top10 = paises.head(10).sort_values()
plt.figure(figsize=(9, 5))
plt.barh(top10.index, top10.values, color="steelblue")
plt.title("Top 10 países com mais clientes")
plt.xlabel("Quantidade de clientes")
plt.ylabel("País")
plt.tight_layout()
plt.savefig("grafico_top10_paises.png", dpi=150)
plt.show()

df["Subscription Date"] = pd.to_datetime(df["Subscription Date"])

por_ano = df.groupby(df["Subscription Date"].dt.year).size()
por_mes = df.groupby(df["Subscription Date"].dt.month).size()
por_mes_ano = df.groupby(df["Subscription Date"].dt.to_period("M")).size()

print("\nAssinaturas por ano:")
print(por_ano)
print("\nAssinaturas por mês (somando todos os anos):")
print(por_mes)
print("\n5 meses com mais vendas:")
print(por_mes_ano.sort_values(ascending=False).head(5))

plt.figure(figsize=(10, 5))
plt.plot(por_mes_ano.index.astype(str), por_mes_ano.values, marker="o", color="darkgreen")
plt.title("Evolução mensal de assinaturas")
plt.xlabel("Mês")
plt.ylabel("Quantidade de assinaturas")
plt.xticks(range(0, len(por_mes_ano), 3), por_mes_ano.index.astype(str)[::3], rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_evolucao_assinaturas.png", dpi=150)
plt.show()

print("\nTop 5 empresas (mais aparições na base):")
print(df["Company"].value_counts().head(5))