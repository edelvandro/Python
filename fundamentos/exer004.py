'''
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
    possíveis sobre ela.
'''

palavra = input('Digite algo: ')

print('Sua classe é: ', type(palavra))
print('Só tem espaços: ', palavra.isspace())
print('É um numerico: ', palavra.isnumeric())
print('É alfabetico: ', palavra.isalpha())
print('É alfanumerico: ', palavra.isalnum())
print('Está em maiúsculo: ', palavra.isupper())
print('Está em minúsculo: ', palavra.islower())
print('Está captalizada: ', palavra.istitle())
