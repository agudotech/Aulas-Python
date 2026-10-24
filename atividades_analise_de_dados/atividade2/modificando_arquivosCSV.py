import pandas as pd
from pathlib import Path
from tkinter import Tk, filedialog

janela = Tk()
janela.withdraw()

caminho = filedialog.askopenfilename(
    title="Selecione o arquivo funcionarios.csv",
    filetypes=[("Arquivos CSV", "*.csv")]
)

janela.destroy()

if not caminho:
    print("Nenhum arquivo foi selecionado. Programa encerrado.")
    raise SystemExit

caminho = Path(caminho)
pasta = caminho.parent

df = pd.read_csv(caminho, sep=None, engine="python", encoding="utf-8-sig")

df.columns = df.columns.str.strip().str.lower()

necessarias = {"id", "nome", "salario", "cargo"}
faltando = necessarias - set(df.columns)

if faltando:
    print("Estão faltando estas colunas no CSV:", faltando)
    print("Colunas encontradas:", list(df.columns))
    raise SystemExit

df["salario"] = pd.to_numeric(df["salario"], errors="raise")

cargos_altos = df[df["salario"] > 6000].copy()

cargos_altos.to_csv(
    pasta / "cargos_altos.csv",
    index=False,
    sep=";",
    encoding="utf-8-sig"
)

df = df.drop(df.index[:2]).reset_index(drop=True)

if "tempo_empresa" not in df.columns:
    df["tempo_empresa"] = 0
else:
    df["tempo_empresa"] = pd.to_numeric(
        df["tempo_empresa"], errors="coerce"
    ).fillna(0)

df["tempo_empresa"] = df["tempo_empresa"].astype(int)

cargos_existentes = set(df["cargo"].dropna().astype(str).str.strip())

cargos_disponiveis = [
    "Analista de Dados",
    "Desenvolvedor Python",
    "Designer UX",
    "Técnico de Redes",
    "Administrador de Banco de Dados",
    "Analista de Segurança",
    "Especialista em Suporte"
]

cargos_novos = [
    cargo for cargo in cargos_disponiveis
    if cargo not in cargos_existentes
][:3]

if len(cargos_novos) < 3:
    print("Não foi possível encontrar três cargos novos.")
    print("Adicione cargos diferentes à lista cargos_disponiveis.")
    raise SystemExit

ids = pd.to_numeric(df["id"], errors="raise")
proximo_id = int(ids.max()) + 1 if not df.empty else 1

novos = pd.DataFrame([
    {
        "id": proximo_id,
        "nome": "Lucas Mendes",
        "salario": 6500,
        "cargo": cargos_novos[0],
        "tempo_empresa": 12
    },
    {
        "id": proximo_id + 1,
        "nome": "Mariana Costa",
        "salario": 7200,
        "cargo": cargos_novos[1],
        "tempo_empresa": 8
    },
    {
        "id": proximo_id + 2,
        "nome": "Pedro Alves",
        "salario": 4500,
        "cargo": cargos_novos[2],
        "tempo_empresa": 6
    }
])

df = pd.concat([df, novos], ignore_index=True)

estagiario = pd.DataFrame([{
    "id": proximo_id + 3,
    "nome": "Ana Souza",
    "salario": 1800,
    "cargo": "Estagiário",
    "tempo_empresa": 3
}])

df = pd.concat([df, estagiario], ignore_index=True)

df["tempo_empresa"] = df["tempo_empresa"].astype(int)

df.to_csv(
    caminho,
    index=False,
    sep=";",
    encoding="utf-8-sig"
)

conferido = pd.read_csv(caminho, sep=";", encoding="utf-8-sig")
altos = pd.read_csv(
    pasta / "cargos_altos.csv",
    sep=";",
    encoding="utf-8-sig"
)

print("\n=== FUNCIONÁRIOS ATUALIZADOS ===")
print(conferido.to_string(index=False))

print("\n=== CONFERÊNCIA ===")
print("Total de funcionários:", len(conferido))
print("Coluna tempo_empresa inteira:",
      pd.api.types.is_integer_dtype(conferido["tempo_empresa"]))
print("Estagiário cadastrado:",
      (conferido["cargo"] == "Estagiário").any())
print("Arquivo atualizado salvo:", caminho)
print("Arquivo de salários altos salvo:", pasta / "cargos_altos.csv")
print("Todos os salários do arquivo cargos_altos.csv são > 6000:",
      (altos["salario"] > 6000).all())

print("\nPrograma executado!")
