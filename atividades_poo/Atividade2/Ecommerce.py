class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade
        else:
            print("Erro: Quantidade inválida")

    def realizar_venda(self, quantidade):
        if quantidade > 0 and quantidade <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantidade
        elif quantidade > self.__quantidade_estoque:
            print("Venda negada: Estoque insuficiente")
        else:
            print("Erro: Quantidade inválida")

    def aplicar_desconto(self, percentual):
        if percentual > 0 and percentual <= 80:
            self.__preco = self.__preco * (1 - percentual / 100)
        else:
            print("Erro: Desconto inválido")

    def exibir_resumo(self):
        print("Nome:", self.__nome)
        print("Preço: R$", self.__preco)
        print("Estoque:", self.__quantidade_estoque)


# Criando o produto
meu_produto = Produto("Notebook", 3000, 10)


# 1. Tentativa de alterar os atributos diretamente
meu_produto.__quantidade_estoque = -50
meu_produto.__preco = -100


# 2. Tentativa de vender mais do que existe no estoque
meu_produto.realizar_venda(9999)


# 3. Mostrar o resumo final
meu_produto.exibir_resumo()


# Mostrar as informações internas do objeto
print("\nInformações internas:")
print(meu_produto.__dict__)
