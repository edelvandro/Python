'''
    Crie um programa que faça o computador jogar JOKENPÔ com você.
'''

from random import randint
from time import sleep

print(' ** Jogo JOKENPÔ **')
computador = randint(0, 2)

print('Escolha sua opção: ')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')

# verificando a opção do jogador
jogador = int(input('Qual é a sua jogada? '))
if jogador == 0 or jogador == 1 or jogador == 2:
    print('')
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ !!!')
    sleep(1)

    print('-=' * 15)
    print('Você jogou {}'.format(jogador))
    print('Computador jogou {}'.format(computador))
    print('-=' * 15)

    # comparando os resultados
    if jogador == computador:
        print('EMPATE')
    elif jogador == 0 and computador == 1:
        print('O COMPUTADOR ganhou.')
    elif jogador == 0 and computador == 2:
        print('VOCÊ Ganhou.')
    elif jogador == 1 and computador == 0:
        print('VOCÊ Ganhou.')
    elif jogador == 1 and computador == 2:
        print('O COMPUTADOR ganhou.')
    elif jogador == 2 and computador == 0:
        print('O COMPUTADOR ganhou.')
    elif jogador == 2 and computador == 1:
        print('VOCÊ Ganhou.')
else:
    print('VALOR INVÁLIDO jogue novamente.')
