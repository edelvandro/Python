'''
    Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos desssa
    progressão.
'''

print('==' * 15)
print('     10 TERMOS DE UMA PA ')
print('==' * 15)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{} -> '.format(c), end=' ')
print('Acabou')
