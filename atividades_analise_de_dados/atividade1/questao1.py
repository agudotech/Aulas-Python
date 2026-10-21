
import pandas as pd

df = pd.read_csv("funcionarios.csv", sep=";")

print("\n--- filtro de salário ---")
filtro_salarios = df[
    (df["salario"] < 3000) |
    (df["salario"] > 5000) |
    (df["salario"] == 3100)
]
print(filtro_salarios)

print("\n--- filtro de cargo ---")
cargos = [
    "Analista de Dados",
    "Analista de Sistemas",
    "Desenvolvedor Java",
    "Cientista de Dados"
]
filtro_cargos = df[df["cargo"].isin(cargos)]
print(filtro_cargos)

print("\n--- salarios maiores que R$6.000 ---")
filtro_6000 = df.loc[
    df["salario"] > 6000,
    ["nome", "cargo"]
]
print(filtro_6000)

print("\n--- FUNCIONÁRIOS COM ID PAR ---")
filtro_id_par = df[df["id"] % 2 == 0]
print(filtro_id_par)
