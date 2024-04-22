# Calculadora

print('Bem vindo(a) a calculadora!')
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
operacao = input('Selecione uma operação (+, -, /, *): ')

if operacao == "+":
    resultado = n1 + n2
    print('O resultado é: ', resultado)
elif operacao == "-":
    resultado = n1 - n2
    print('O resultado é: ', resultado)
elif operacao == "/":
    resultado = n1 / n2
    print('O resultado é: ', resultado)
elif operacao == "*":
    resultado = n1 * n2
    print('O resultado é: ', resultado)
else:
    print('Operação inválida.')
