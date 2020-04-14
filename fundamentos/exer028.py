'''
    Escreva um programa que faça o computador pensar em um numero inteiro de 0 a 5,
    e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
    O programa deverá esrever na tela se o usuário venceu ou não.
'''

import random             # ou from random import randint
from time import sleep

numero_pensado = random.randint(0, 5)
numero_escolhido = int(input('Tente adivihar o número que o computador escolheu. Digite um número de 0 a 5: '))
print('Processando...')
sleep(2)
if numero_pensado == numero_escolhido:
    print('Parabéns, acertô miseravi!')
else:
    print('Errouuuuuu, boa sorte da próxima vez!')
