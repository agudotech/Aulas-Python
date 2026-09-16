# CALCULADORA BÁSICA DE DOIS NÚMEROS

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operador = input("Digite o operador (+, -, * ou /): ")

if operador == "+":
    print("Resultado:", num1 + num2)
elif operador == "-":
    print("Resultado:", num1 - num2)
elif operador == "*":
    print("Resultado:", num1 * num2)
elif operador == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Não é possível dividir por zero!")
else:
    print("Operação inválida!")
