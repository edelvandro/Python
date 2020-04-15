'''
    Crie um programa que leia o ano de nascimento de sete pessoas.
    No final, mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores.
'''

from datetime import date

# contadores
maior = 0
menor = 0

for i in range(1, 8):
    ano = int(input('Digite o ano que a {} pessoa nasceu: '.format(i)))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('\nAo todo tivemos {} pessoa(s) maior(es) de idade.'.format(maior))
print('E tambem tivemos {} pessoa(s) menor(es) de idade.'.format(menor))
