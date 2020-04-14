# Escreva um programa que escreva uma temperatura digitada em  °C e converta para °F.


c = float(input('Digite a temperatura em °C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}°C corresponde a  {:.2f}°F!'.format(c, f))
