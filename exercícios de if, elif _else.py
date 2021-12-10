#exercícios de if, elif e else

"""
Faça um programa que peça dois números e imprima o maior deles.
"""

nu1=int(input('NUMERO 1 : '))
nu2=int(input('NUMERO 2 : '))

if nu1 > nu2 :
    print(f'{nu1} é maior {nu2}')
elif nu2 > nu1 :
    print(f'{nu2} é maior que {nu1} ')
elif nu1 == nu2 :
    print('os numeros são iguais')
else :
    print('ERRO')
