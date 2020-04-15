# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):          # faz um range do 1 até o total de numeros digitados.
    if numero % c == 0:                 # se o resto da divisão do numero pelo índice do FOR resultar em 0.
        print('\033[33m', end='')
        total += 1                      # acrescenta 1 ao contador.
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end=' ')
print('\n\033[mO número {} foi divido {} vezes'.format(numero, total))
if total == 2:
    print('E por isso ele É Primo')
else:
    print('E por isso ele NÂO É PRIMO')
