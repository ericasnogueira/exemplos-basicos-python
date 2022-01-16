"""
Listas importantes a partir do Dicionário


Métodos importantes:
    .keys() -> uma 'lista' com todas as chaves do dicionario
    .values() -> uma 'lista' com todos os valores do dicionario
OBS: Se o dicionario for modificado,automaticamente essas variáveis são modificadas,mesmo 
tendo sido criadas anteriormente
"""

vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

chaves = vendas_tecnologia.keys() #pegando só as chaves
valores = vendas_tecnologia.values() #pegando só os valores
print(chaves)
print(valores)

#para não aparecer o nome key e values
print(list(chaves))
print(list(valores))

"""
For vai fucionar normal em dict_listas,porque não deixa de ser uma lista de itens que 
poder ser percorrida(itarable), mas o que aprendemos de lista não necessariamente se aplicam 
a essas dict_listas.


    Para transformar as dict_listas em listas normais, usamos a função list.

    º lista_chaves=list(dicionario.keys())
    º Pode ser útil caso a gente queira fazer alguma organização das chaves. EX: imprimir uma
    lista com os valores em ordem alfabética, de forma que todas as tvs fiquem juntas, todos
    os iphone/ipad também e assim vai :
"""

for chave in vendas_tecnologia:
    print(f'{chave} : {vendas_tecnologia[chave]} unidades')
print('-'*40)

#Agora se quisermos orgranizer isso, fazemos: 
lista_chaves = list(chaves)
lista_chaves.sort()

for chave in lista_chaves:
    print(f'{chave} : {vendas_tecnologia[chave]} unidades')

