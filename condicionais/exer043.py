'''
    Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status,
    de acordo com a tabela abaixo.

    Abaixo de 18.5: Abaixo do peso.
    Entre 18.5 e 25: Peso ideal.
    Entre 25 e 30: Sobrepeso.
    Entre 30 e 40: Obesidade.
    Acima de 40: Obesidade Morbida.
'''

altura = float(input('Digite a altura (m): '))
peso = float(input('Digite o peso (Kg) : '))
imc = peso / (altura ** 2)
print('O IMC é: {:.1f}'.format(imc))

if imc <= 18.5:
    print(' ABAIXO do peso.')
elif 18.5 <= imc < 25:  # imc está entre 18.5 e 25.
    print('Peso IDEAL.')
elif 25 <= imc <= 30:
    print('SOBREPESO.')
elif 30 <= imc <= 40:
    print('OBESIDADE.')
elif imc >= 40:
    print('OBESIDADE MORBIDA.')
