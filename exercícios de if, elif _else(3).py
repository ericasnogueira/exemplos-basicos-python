
"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:
infantil A = 5 - 7 anos
// infantil B = 8 - 10 anos
// juvenil A = 11 - 13 anos
// juvenil B = 14 - 17 anos
// sênior = maiores de 18

"""


idade_n=int(input('Qual é a idade do nadador : '))

if idade_n < 5 :
   print('sem classificação')
elif idade_n <=7 :
    print('infantil A')
elif idade_n <=10 :
    print('infantil B')
elif idade_n <=13 :
    print('juvenil A')
elif idade_n <=17 :
    print('juvenil B')
else : 
    print('sênior')
    
