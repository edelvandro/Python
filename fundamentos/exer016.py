# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.


'''
numero = float(input('Digite um numero: '))
resultado = numero // 1
print('O numero {} tem a parte inteira {}'.format(numero, int(resultado)))
'''

# Para utilizar a função trunk é necessario importar a biblioteca "math".

import math
numero = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(numero, math.trunc(numero)))
