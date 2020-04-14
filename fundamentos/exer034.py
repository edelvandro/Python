'''
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    Para salários superiores a R$1.250,00, calcule um aumento de 10%.
    Para os inferiores ou iguais, o aumento será de 15%.
'''

salario = float(input('Digite o valor do salário atual: R$'))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print('Seu salário com o aumento será de R${:.2f}.'.format(novo))
