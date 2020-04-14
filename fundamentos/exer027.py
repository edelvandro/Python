'''
    Faça um programa que leia o nome completo de uma pessoa,
    mostrando em seguida o primeiro e o último nome separadamente.
'''

entrada = str(input('Digite um nome completo: ')).strip()
print('Olá {}'.format(entrada))
nome = entrada.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome) - 1]))
