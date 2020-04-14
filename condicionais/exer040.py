'''
    Crie um programa que leia as duas notas de um aluno e calcule sua média, mostando uma mensagem no final,
    de acordo com a média atingida:
    Media abaixo de 5.0: REPROVADO
    Média entre 5.0 e 6.9 RECUPERAÇÃO
    Média 7.0 ou superior: APROVADO
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media <= 5.0:
    print('A média ente as notas {} e {} foi {}, você foi REPROVADO.'.format(nota1, nota2, media))
elif media >= 5.1 and media <= 6.9:
    print('A média entre as notas {} e {} foi {}, você esta de RECUPERAÇÂO.'.format(nota1, nota2, media))
else:
    print('A média entre as notas {} e {} foi {}, Parabéns você foi APROVADO!'.format(nota1, nota2, media))
