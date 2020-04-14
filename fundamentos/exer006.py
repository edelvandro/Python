# Crie um programa que leia um número e mostre o seu dobro o triplo e a raiz quadrada.

num = int(input('Digite um numero: '))

'''
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** (1/2)

print('O dobro de', num, 'é', dobro)
print('O triplo de', num, 'é', triplo)
print('O raiz quadrada de {} é {:.2f}.'.format(num, raiz_quadrada)) 

print('O dobro de {} vale: {} \nO triplo de {} vale: {} \nA raiz quadrada de {} vale: {:.2f}'.format(num, (num * 2),
    num, (num * 3), num, (num ** (1/2)))) 
'''
# refatorado

print('O dobro de {} vale: {} \nO triplo de {} vale: {} \nA raiz quadrada de {} vale: {:.2f}'
      .format(num, (num * 2), num, (num * 3), num, (pow(num, 1 / 2))))
