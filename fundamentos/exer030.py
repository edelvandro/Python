# Crie um programa que leia um número inteiro na tela e mostre se ele é par ou ímpar.

numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))
