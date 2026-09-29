from abc import ABC, abstractmethod

class Transporte(ABC):

    def iniciar_processo(self):
        print("Sistema central: operação de cálculo de frete iniciada.")

    @abstractmethod
    def calcular_frete(self, distancia, peso):
        pass


class Caminhao(Transporte):

    def calcular_frete(self, distancia, peso):
        valor = distancia * 5

        if peso <= 10000:
            print(f"Frete por caminhão: R$ {valor:.2f}")
        else:
            print("Erro: o caminhão não suporta cargas acima de 10.000 kg.")

class Drone(Transporte):

    def calcular_frete(self, distancia, peso):
        if peso <= 2:
            valor = distancia * 20
            print(f"Frete por drone: R$ {valor:.2f}")
        else:
            print("Erro: o drone suporta no máximo 2 kg.")

def processar_lote(lista_de_objetos):
    for item in lista_de_objetos:
        item.iniciar_processo()
        item.calcular_frete(10, 1.5)
        print("-" * 30)


# ==================================================
# TESTES
# ==================================================

# 1. Tentativa de instanciar a Classe Abstrata
# Descomente para testar e provar que o Python bloqueia:
# objeto_generico = Transporte()


# 2. Instanciando as Classes Filhas
obj1 = Caminhao()
obj2 = Drone()


# 3. Criando um Lote de Processamento
lote = [obj1, obj2, obj1]


# 4. Processando em lote
print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")
processar_lote(lote)
