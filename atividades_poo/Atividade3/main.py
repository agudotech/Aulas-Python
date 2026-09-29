from atividades_poo.Atividade3.Atividade3 import mamifero

baleia = mamifero("Baleia", idade=10,
                  velocidade_kmh=30)
print("===Estado inicial da baleia===")
baleia.exbir_resumo()

print("\n===Alimentando===")
baleia.alimentar(40)
baleia.exbir_resumo()

print("\n===Correndo===")
baleia.correr()
baleia.exbir_resumo()

print("\n===Som===")
baleia.emitir_som()

print("\n===Tentando idade inválida===")
baleia.idade = -5

print("\n===Tentando porção inválida===")
baleia.alimentar(10)
baleia.alimentar(0)