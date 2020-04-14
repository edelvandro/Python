# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

'''
numero = int(input('Digite um número: '))
sucessor = numero + 1
antecessor  = numero - 1
print('O antecessor do numero {} é {} e o sucessor é {}'.format(numero, antecessor, sucessor))
'''

# refatorado

numero = int(input('Digite um numero: '))
print('O numero digitado foi: {}, seu antecessor é {} e seu sucessor é {}:'.format(numero, numero - 1, numero + 1))
