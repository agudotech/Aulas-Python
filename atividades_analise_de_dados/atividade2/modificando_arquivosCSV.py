import pandas as pd

df = pd.read_csv("funcionarios.csv", sep=";", encoding="utf-8-sig")

print("\n========== DADOS ORIGINAIS ==========")
print(df.to_string(index=False))
print(f"\nTotal de funcionários: {len(df)}")

df = df.drop(index=[0, 1]).reset_index(drop=True)

print("\n========== APÓS REMOVER OS DOIS PRIMEIROS ==========")
print(df.to_string(index=False))
print(f"\nTotal de funcionários: {len(df)}")

novos_funcionarios = pd.DataFrame([
    {
        "id": 31,
        "nome": "Lucas Martins",
        "salario": 7200,
        "cargo": "Arquiteto de Software"
    },
    {
        "id": 32,
        "nome": "Mariana Costa",
        "salario": 5800,
        "cargo": "Especialista em UX"
    },
    {
        "id": 33,
        "nome": "Pedro Henrique",
        "salario": 8500,
        "cargo": "Engenheiro de Dados"
    }
])

df = pd.concat([df, novos_funcionarios], ignore_index=True)

df["tempo_empresa"] = [int(valor) for valor in
                       range(1, len(df) + 1)]

df["tempo_empresa"] = df["tempo_empresa"].astype(int)

estagiario = pd.DataFrame([{
    "id": 34,
    "nome": "Julia Santos",
    "salario": 1500,
    "cargo": "Estagiário",
    "tempo_empresa": 3
}])

df = pd.concat([df, estagiario], ignore_index=True)

df["tempo_empresa"] = df["tempo_empresa"].astype(int)

cargos_altos = df[df["salario"] > 6000].copy()

cargos_altos.to_csv(
    "cargos_altos.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print("\n========== FUNCIONÁRIOS COM SALÁRIO ACIMA DE R$ 6.000 ==========")
print(cargos_altos.to_string(index=False))
print(f"\nTotal encontrado: {len(cargos_altos)}")

df.to_csv(
    "funcionarios.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print("\n========== DADOS FINAIS ==========")
print(df.to_string(index=False))

print("\n========== VERIFICAÇÃO ==========")
print(f"Total de funcionários: {len(df)}")
print(f"Total com salário acima de R$ 6.000: {len(cargos_altos)}")
print(f"Coluna tempo_empresa: {df['tempo_empresa'].dtype}")
print(f"Existe funcionário Estagiário: "
      f"{(df['cargo'] == 'Estagiário').any()}")

print("\nArquivos salvos:")
print("- funcionarios.csv (dados atualizados)")
print("- cargos_altos.csv (salários acima de R$ 6.000)")
