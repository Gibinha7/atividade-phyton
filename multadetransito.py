velocidade = float(input('Digite a velocidade do carro: '))
if velocidade <=80:
    print('ok, sem problemas')
elif velocidade > 80:
    print('Voce será multado!')
    qtdemulta = velocidade - 80.0
    valormulta = qtdemulta * 7
    print("Voce pagará R${:.2f}".format(valormulta))
    print('Fim do programa!')