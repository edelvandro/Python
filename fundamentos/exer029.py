'''
    Escreva um programa que leia a velocidade de um carro.
    Se esse ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada km acima do limite.
'''

velocidade = int(input('Digite a velocidade do carro: '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Parabéns, continue sempre dirigindo com segurança!')
else:
    print('Voce esta a {}km/h, voce excedeu o limite em {}km/h e foi multado no valor de R${:.2f}.'
        .format(velocidade, velocidade - 80, multa))
