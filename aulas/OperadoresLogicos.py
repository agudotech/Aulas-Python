#OPERADORES
"""
    ATRIBUIÇÃO
    = -> variavel = 10

    ! = NÃO, NOT, CONTRÁRIO...

    COMPARAÇÃO
    != ->  se for diferente retorna True, se for igual retorna False

    == ->  se for diferente retorna False, se for igual retorna True

    > ->  se for maior retorna True, se for menor retorna False

    < ->  se for menor retorna False, se for maior retorna True

    >= ->  se for maior e igual retorna True, contrario retorna False

    <= ->  se for menor e igual retorna False, contrario retorna True

    PARA MAIS COMPARAÇÕES
    and -> se todas as comparações forem True, retorna True

    or -> se ao menos uma das comparações for True, retorna True

    not ->

"""

#TESTES
idade = 18
print("Nossa balada, não aceita criança, nem idoso e nem pais dos convidados")
print("voce pode entrar em uma balada?")
print( (idade >= 18) and (idade < 65) and (idade == 18))