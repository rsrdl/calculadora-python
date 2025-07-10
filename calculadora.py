# Calculadora
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input('Digitea operação desejada (+, -, *, /): ')

match operacao:
    case '+':
        resp = num1 + num2
    case '-':
        resp = num1 - num2
    case '*':
        resp = num1 * num2
    case '/':
        if num2 == 0:
            resp = "Erro: Divisão por zero não é permitida."
        else:
            resp = num1 / num2
    case _:
        resp = "Operação inválida."

print(f'O resultado da operação é: {resp}')