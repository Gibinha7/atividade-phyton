def encontrar_maior_menor(dicionario):
    """
    Encontra o maior e o menor valor em um dicionário.
    """
    if not dicionario:
        return None, None  # Retorna None, None se o dicionário estiver vazio

    valores = dicionario.values()
    maior_valor = max(valores)
    menor_valor = min(valores)

    return maior_valor, menor_valor


def obter_dicionario_do_usuario():
    """
    Solicita ao usuário que insira pares de chave e valor para criar um dicionário.
    """
    dicionario = {}
    print("Digite os pares de chave e valor para o dicionário.")
    print("Digite 'sair' como chave para encerrar a entrada.")

    while True:
        chave = input("Digite a chave: ")
        if chave.lower() == 'sair':
            break
        valor = input("Digite o valor (numérico): ")

        try:
            # Tenta converter o valor para um número (float)
            valor = float(valor)
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
            continue

        dicionario[chave] = valor

    return dicionario


# Obtém o dicionário do usuário
dicionario_usuario = obter_dicionario_do_usuario()

# Verifica se o dicionário não está vazio
if dicionario_usuario:
    maior, menor = encontrar_maior_menor(dicionario_usuario)
    print(f"O maior valor é: {maior}")
    print(f"O menor valor é: {menor}")
else:
    print("O dicionário está vazio. Nenhum valor para comparar.")
