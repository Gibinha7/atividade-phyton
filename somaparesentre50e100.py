def somadospares(num1, num2):
    soma = 0
    for num in range(num1, num2 + 1):
        if num % 2 == 0:  # Verifica se o número é par
            soma += num
    return soma

#  intervalo
num1 = 50
num2 = 100

# Chama a função e armazena o resultado
resultado = somadospares(num1, num2)

# Imprime o resultado
print("A soma dos números pares entre", num1, "e", num2, "é:", resultado)
