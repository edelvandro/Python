# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.


from math import sin, cos, tan, radians
            # Ao importar apenas as bibliotecas necessárias não utiliza o método math nas chamadas.

angulo = float(input('Digite o valor do angulo: '))
print('O valor do seno é {:.2f}'.format(sin(radians(angulo))))
print('O valor do cosseno é {:.2f}'.format(cos(radians(angulo))))
print('O valor da tangente é: {:.2f}'.format(tan(radians(angulo))))
