# Explicação do erro: a função input() retorna uma string (ex: "1234"),
# enquanto a senha cadastrada é um número inteiro (1234).
# A comparação entre int e str resulta em False. 
# Para corrigir, convertemos a entrada do usuário para int usando int().

senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: "))

acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)