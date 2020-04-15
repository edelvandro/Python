'''
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
    peça a digitação novamente até um valor correto.
'''

sexo = str(input('Informe o sexo: [M/F] ')).strip().upper()[0]

while sexo  not in 'MF':
    sexo = str(input('Dados inválidos, por favor informe seu sexo: [M/F]')).strip().upper()[0] # apenas a primeira letra
print('Sexo {} registrado com sucesso.'.format(sexo))

