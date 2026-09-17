# CONHECENDO FUNÇÕES NO PYTHON

# retorna um valor -> precisar desse valor
def soma():
    print("Fazendo uma soma.")
    numero1 =  int(input("Numero 1: "))
    numero2 = int(input("Numero 2: "))
    return print(numero1 + numero2)
# função vazia -> não retorna nada, mas executa algo
def multiplicacao():
    print("Fazendo uma multiplicacao.")
    numero1 = int(input("Numero 1: "))
    numero2 = int(input("Numero 2: "))
    return print(numero1 * numero2)

def olaUsuario (nome):
    print(f"Olá {nome}!")