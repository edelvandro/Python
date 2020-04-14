# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário atual: R$ '))
novo_salario = salario + (salario * (15 / 100))
print('O salário de {} com 15% de aumento será R${:.2f}'.format(salario, novo_salario))
