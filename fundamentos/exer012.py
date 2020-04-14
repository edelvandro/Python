# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

'''
valor = float(input('Digite vo valor do produto: R$ '))
desconto = valor * (5 / 100)
total = valor - desconto
print('O valor do produto que custava {} com descoto de 5% vai custar: R${:.2f}'.format(valor, total))
'''


# refatorado

valor = float(input('Digite vo valor do produto: R$ '))
novo_valor = valor - (valor * (5 / 100))
print('O valor do produto que custava {} com descoto de 5% vai custar: R${:.2f}'.format(valor, novo_valor))
