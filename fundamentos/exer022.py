'''
    Crie um programa que leia o nome completo de uma pessoa e mostre,
    o nome com todas as letras maiúsculas, o nome com todas minúsculas
    Quantas letras tem no total (sem considerar espaços).
'''

nome = str(input('Digite o nome completo: ')).strip()
print('O nome digitado, em letras maiusculas é: {}'.format(nome.upper()))
print('O nome digitado, em letras munisculas é: {}'.format(nome.lower()))

# len mostra o tamaho da string, nome.count conta quantos espaços em branco tem e diminui.
print('O nome tamanho do nome sem considerar os espaços é: {}'.format(len(nome) - nome.count(' ')))

separa = nome.split()
print('O primeiro nome tem {} letras'.format(len(separa[0])))
