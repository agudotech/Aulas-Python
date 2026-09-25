from Atividade3 import mamifero, Animal

baleia = mamifero("Baleia", idade=10, velocidade_kmh=30)
print("===Estado inicial da baleia===")
baleia.exbir_resumo()

print("\n===Alimentando===")
baleia.alimentar(40)
baleia.exbir_resumo()

print("\n===Correndo===")
baleia.correr()
baleia.exbir_resumo()

print("\n===Som===")
