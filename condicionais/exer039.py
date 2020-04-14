'''
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
    se ele ainda vai se alistar ou se ja passou do tempo do alistamento.
    Seu programa tambem deverá mostrar e tempo que falta ou o tempo que passou do prazo.
'''

from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
print('Voce tem {} anos'.format(idade))
if idade == 18:
    print('Esta na hora de você se alistar!')
elif idade < 18:
    tempo = 18 - idade
    alistamento = date.today().year + tempo
    print('Ainda faltam {} anos para você se alistar'.format(tempo))
    print('Seu alistamento será em {}.'.format(date.today().year + tempo))
elif idade > 18:
    tempo = idade - 18
    print('Faz {} anos que você já deveria ter se alistado'.format(tempo))
    print('Seu alistamento foi em {}.'.format(date.today().year - tempo))
