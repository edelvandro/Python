'''
    Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal,e condição
    de pagamento:

    À vista dinheiro / cheque: 10% de desconto.
    À vista no cartão: 5% de desconto.
    Em até 2x no cartão: preço normal.
    3x ou mais no cartão: 20% de juros.
'''

print('=' * 5 + ' LOJA PYTHON ' + '=' * 5)
preco = float(input('Digite o preço do produto: R$ '))
print('FORMA DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] á vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print('O valor de sua compra com pagamento a vista será de R${:.2f}'.format(preco -(preco * 10 / 100)))
elif opcao == 2:
    print('O valor de sua compra com pagamento a vista no cartão será de R${:.2f}'.format(preco - (preco * 5 / 100)))
elif opcao == 3:
    print('O valor de sua compra com pagamento parcelado em 2 vezes no cartão será de R${:.2f}'.format(preco))
elif opcao == 4:
    print('O valor de sua compra com pagamento parcelado em 3x ou mais será de R${:.2f}'.format(preco + (preco * 20 / 100)))
else:
    print('Opção Inválida')
