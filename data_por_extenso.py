def pdata():
    while True:
        data = input("Digite uma data no formato DD/MM/AAAA: ")
        try:
            dia, mes, ano = map(int, data.split('/'))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and len(str(ano)) == 4:
                return dia, mes, ano
            else:
                print("Data no formato inválido.")
        except ValueError:
            print("Data no formato incorreto.")


def numero_por_extenso(num):
    unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    especiais = ["onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

    if num < 10:
        return unidades[num]
    elif 10 < num < 20:
        return especiais[num - 11]
    elif num < 100:
        d, u = divmod(num, 10)
        return f"{dezenas[d]} e {unidades[u]}" if u > 0 else dezenas[d]
    elif num < 1000:
        c, resto = divmod(num, 100)
        centena = "cem" if c == 1 and resto == 0 else f"{unidades[c]} cento"
        return f"{centena} e {numero_por_extenso(resto)}" if resto > 0 else centena
    elif num < 10000:
        milhar, resto = divmod(num, 1000)
        return f"{numero_por_extenso(milhar)} mil {numero_por_extenso(resto)}" if resto > 0 else f"{numero_por_extenso(milhar)} mil"
    else:
        return "número fora do intervalo"


def extenso(dia, mes, ano):
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]

    dias_extenso = [
        "primeiro", "dois", "três", "quatro", "cinco", "seis",
        "sete", "oito", "nove", "dez", "onze",
        "doze", "treze", "quatorze", "quinze",
        "dezesseis", "dezessete", "dezoito", "dezenove",
        "vinte", "vinte e um", "vinte e dois", "vinte e três",
        "vinte e quatro", "vinte e cinco", "vinte e seis", "vinte e sete",
        "vinte e oito", "vinte e nove", "trinta", "trinta e um"
    ]

    dia_extenso = dias_extenso[dia - 1] if dia <= 31 else "dia inválido"
    mes_extenso = meses[mes - 1]
    ano_extenso = numero_por_extenso(ano)
    return f"{dia_extenso} de {mes_extenso} de {ano_extenso}"


def menu():
    print("""
    1 - Converter uma data para por extenso
    2 - Mostrar a última data convertida
    3 - Sair do programa
    """)


def main():
    ultima_data = None
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            dia, mes, ano = pdata()
            ultima_data = extenso(dia, mes, ano)
            print("Data por extenso:", ultima_data)
        elif escolha == '2':
            if ultima_data:
                print("Última data convertida:", ultima_data)
            else:
                print("Nenhuma data foi convertida ainda.")
        elif escolha == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()



