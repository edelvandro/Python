# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year  # Mostra o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # Ocorre a cada 4 ano, exceto multiplos de 100 ou multiplos de 400
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print("O ano {} NÂO é BISSEXTO.".format(ano))
