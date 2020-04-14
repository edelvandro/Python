'''
    Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
    nome delas e escrevendo o nome do escolhido.
'''

import random  # ou from random import choice.

primeiro_aluno = input('Primeiro aluno: ')
segundo_aluno = input('Segundo aluno: ')
teceiro_aluno = input('Terceiro aluno: ')
quarto_aluno = input('Quarto aluno: ')

lista = [primeiro_aluno, segundo_aluno, teceiro_aluno, quarto_aluno]
escolhido = random.choice(lista)                                        # escolhido =  random.escolhe(na lista)
print('O aluno escolhido foi {}'.format(escolhido))
