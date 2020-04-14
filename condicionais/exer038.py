'''
    Escreva um programa qe leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    O primeiro valor é maior.
    O segundo valor é maior.
    Não existe valor maior, os dois são iguais.
'''

valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))

if valor1 > valor2:
    print('O primeiro valor é maior.')
elif valor2 > valor1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
