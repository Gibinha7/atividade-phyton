km = float(input('Qual é a distância da sua viagem? '))
if km > 200.0:
    valorpassagem = km * 0.45
elif km <= 200.0:
    valorpassagem = km * 0.50
print('O valor da passagem é R${:.2f}'.format(valorpassagem))