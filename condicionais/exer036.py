'''
    Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
    O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então empréstimo será negado.
'''

valor_casa = float(input('Digite o valor da casa:R$ ').strip())
salario = float(input('Digite o valor do salário:R$ ').strip())
anos = int(input('Digite em quantos anos deseja pagar: ').strip())

valor_parcela = valor_casa / (anos * 12)
valor_maximo = salario * (30 / 100)

if valor_parcela >= valor_maximo:
    print(
        ' "FINANCIAMENTO NEGADO" O valor da parcela será de R${:.2f} e excede ao máximo permitido que é de R${:.2f}.'
            .format(valor_parcela, valor_maximo))
else:
    print('Parabéns seu emprestimo foi aprovado, o valor da parcela será de: R${:.2f} reais.'.format(valor_parcela))
