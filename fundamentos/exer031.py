'''
    Desenvolva um programa que pergunte a distância de uma viagem em KM.
    Calcule o preço da passagem, cobrando R$0,50 por KM para viagens até 200KM e R$0,45 para viagens mais longas.
'''

distancia = int(input('Digite a distância de sua viagem: '))

if distancia <= 200:
    print('O valor de sua passagem será: R${:.2f}.'.format(distancia * 0.50))
else:
    print('O valor de sua passagem será: R${:.2f}.'.format(distancia * 0.45))
