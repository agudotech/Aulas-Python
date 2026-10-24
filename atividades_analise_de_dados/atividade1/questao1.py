import pandas as pd

df = pd.read_csv("funcionarios.csv", sep=";")

def exibir_resultado(titulo, dados):
    print("\n" + "=" * 65)
    print(f"{titulo:^65}")
    print("=" * 65)

    if dados.empty:
        print("Nenhum funcionário encontrado.")
    else:
        print(dados.to_string(index=False))
        print("-" * 65)
        print(f"Total de funcionários encontrados: {len(dados)}")

filtro_salarios = df[
    (df["salario"] < 3000) |
    (df["salario"] > 5000) |
    (df["salario"] == 3100)
]

exibir_resultado("FILTRO DE SALÁRIOS", filtro_salarios)

cargos = [
    "Analista de Dados",
    "Analista de Sistemas",
    "Desenvolvedor Java",
    "Cientista de Dados"
]

filtro_cargos = df[df["cargo"].isin(cargos)]

exibir_resultado("FILTRO DE CARGOS", filtro_cargos)

filtro_6000 = df.loc[
    df["salario"] > 6000,
    ["nome", "cargo"]
]

exibir_resultado("SALÁRIOS ACIMA DE R$ 6.000", filtro_6000)

filtro_id_par = df[df["id"] % 2 == 0]

exibir_resultado("FUNCIONÁRIOS COM ID PAR", filtro_id_par)

print("\n" + "=" * 65)
print(f"{'RESUMO GERAL':^65}")
print("=" * 65)
print(f"Total de funcionários cadastrados: {len(df)}")
print(f"Salários filtrados:                 {len(filtro_salarios)}")
print(f"Cargos selecionados:                {len(filtro_cargos)}")
print(f"Salários acima de R$ 6.000:         {len(filtro_6000)}")
print(f"Funcionários com ID par:             {len(filtro_id_par)}")
print("=" * 65)

