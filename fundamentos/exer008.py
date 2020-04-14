# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

num = float(input('Digite um valor: '))
print('A medida de {} corresponde a \n{}km\n{}dc\n{}hm\n{}dc\n{}cm\n{}mm'.format(num, (num / 1000), (num / 100),
                                                                                 (num / 10), (num * 10), (num * 100),
                                                                                 (num * 1000)))
