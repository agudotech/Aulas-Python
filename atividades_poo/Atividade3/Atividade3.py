from atividades_lp.Atividade3.Calculadora import valor


class Animal:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__nivel_fome = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if valor < 0:
            print("Erro: idade inválida")
        else:
            self.__idade = valor

    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self, valor):
        if valor < 0:
            self.__nivel_fome = 0
        elif valor > 100:
            self.__nivel_fome = 100
        else:
            self.__nivel_fome = valor

    def alimentar(self, porcao):
        if porcao < 0:
            print("Erro: opção inválida")
        else:
            self.nivel_fome = self.nivel_fome - porcao

    def emitir_som(self):
        print(f"{self.nome} faz um som genérico.")

    def exibir_resumo(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Fome: {self.nivel_fome}")


class mamifero(Animal):
    def __init__(self, nome, idade, velocidade_kmh):
        super().__init__(nome, idade)
        self.__velocidade_kmh = velocidade_kmh

    @property
    def velocidade_kmh(self):
        return self.__velocidade_kmh

    def correr(self):
        print(f"{self.nome} correu a {self.velocidade_kmh} kmh!")
        self.nivel_fome = self.nivel_fome + 20

    def emitir_som(self):
        print(f"{self.nome} ruge alto!")

    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Velocidade: {self.velocidade_kmh} kmh.")

    class Ave(Animal):
        def __init__(self, nome, idade, envergadura_asas):
            super().__init__(nome, idade)
            self.__envergadura_asas = envergadura_asas

    @property
    def envergadura_asas(self):
        return self.__envergadura_asas

    def voar(self):
        if self.nivel_fome < 80:
            print(f"{self.nome} voou com suas asas de {self.envergadura_asas}cm!")
            self.nivel_fome = self.nivel_fome + 15
        else:
            print(f"Voo falhou: {self.nivel_nome} está faminto demais pra voar!")

    def emitir_som(self):
            print(f"{self.nome} canta um som muito lindo!")

    def exibir_resumo(self):
            super().exbir_resumo()
            print(f"Envergadura das asas: {self.envergadura_asas} cm")


