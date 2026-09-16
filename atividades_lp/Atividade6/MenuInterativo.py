opcao = 0

while opcao != 2:
    print("======================")
    print("   MENU PRINCIPAL")
    print("======================")
    print("1 - Mostrar saudação")
    print("2 - Sair do programa")
    print()

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        print("\nOlá! Seja muito bem-vindo ao programa!")
        print("É um prazer ter você aqui.")

    elif opcao == 2:
        print("\nPrograma encerrado.")
        print("Obrigado por utilizar o programa!")

    else:
        print("\nOpção inválida!")
        print("Por favor, escolha apenas 1 ou 2.")

print("\nFim do programa.")
