'''
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
    calcule e mostre o comprimento da hipotenuza
'''

'''
cat_oposto = float(input('digite o valor do cateto opostro: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenuza = (cat_oposto**2 + cat_adjacente**2) ** (1/2)
print('O valor da hipotenuza é: {:.2f}'.format(hipotenuza))
'''

import math

cat_oposto = float(input('Digite o valor do cateto opostro: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenuza = math.hypot(cat_oposto, cat_adjacente)
print('O valor da hipotenuza é: {:.2f}'.format(hipotenuza))
