'''
    Melhore o desafio 061, perguntando para o usuário se ele que mostrar mais alguns termos.
    O programa encerra quando ele disser que quer mostrar 0 termos
'''

print("Gerador de PA")
print("-=" * 9)
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
cont = 1
termo = primeiro
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end=" ")
        termo += razao
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Prigressão finalizada com {} termos mostrados.".format(total))
print("FIM")
