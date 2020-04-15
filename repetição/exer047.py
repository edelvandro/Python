'''
    Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 a 50.
'''

'''for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')'''

# Refatorado

for i in range(2, 51, 2):
    print(i, end=' ')
