# Faça um programa que leia tês numeros e mostra qual deles é o maior e qual é o menor.

maior = 0
menor = 0

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# Verificando o número maior

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num1:
    maior = num3

# Verificando o numero menor
menor = num1
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print('O {} é o número maior!'.format(maior))
print('O {} é o número menor!'.format(menor))
