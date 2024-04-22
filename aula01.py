# Criar uma lista com números de 1 a 100
numeros = list(range(1, 101))

# Filtrar os números pares divisíveis por 4
numeros_pares_divisiveis_por_4 = [num for num in numeros if num % 2 == 0 and num % 4 == 0]

# Imprimir os números filtrados
for num in numeros_pares_divisiveis_por_4:
    print(num)
