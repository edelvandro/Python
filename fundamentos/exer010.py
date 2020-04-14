'''
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
    Considere US$ 1.00 = R$ 3,27.
'''

valor = float(input('Digite um valor em real: R$ '))
dolar = 3.27
print('Com R${} você pode comprar US${:.2f}'.format(valor, (valor / dolar)))
