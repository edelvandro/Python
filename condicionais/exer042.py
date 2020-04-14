'''
    Refaça o exercicio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
    Equilatero: todos os lados iguais.
    Isóceles: dois lados iguais.
    Escaleno: todos os lados diferentes.
'''

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
v3 = float(input('Digite o terceiro valor: '))

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('Os segmentos acima PODEM formar um triangulo.')
    if v1 == v2 == v3:
        print('Formam um triangulo EQUILATERO.')
    elif v1 != v2 != v3 != v1:
        print('Formam um triangulo ESCALENO.')
    else:
        print('Formam um triangulo ISÓCELES.')
else:
    print('Os segmentos acima NÂO podem formar um triangulo.')
