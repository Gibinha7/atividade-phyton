def separar_positivos_negativos(lista):
    numerosp = []  # Lista para numeros positivos
    numerosn = []  # Lista para numeros negativos

    for num in lista:
        if num >= 0:
            numerosp.append(num)  # Adiciona o numero positivo na lista de positivos
        else:
            numerosn.append(num)  # Adiciona o numero negativo na lista de negativos

    return numerosp, numerosn


# Recebe a lista de inteiros do usuário
if __name__ == "__main__":
    entrada = input("Digite uma lista de inteiros: ")
    lista = [int(x) for x in entrada.split()]

    numerosp, numerosn = separar_positivos_negativos(lista)

    print("Números positivos:", numerosp)
    print("Números negativos:", numerosn)

