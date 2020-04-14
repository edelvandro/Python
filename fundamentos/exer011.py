'''
    Faça um programa que leia a largura e a altura de uma parede em metros,calcule sua área e a quantidade de tinta
    necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
'''

largura = float(input('Digite a largua da parede: '))
altura = float(input('Digite a altura da parede '))

area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {} litros de tinta.'.format(tinta))
