"""
Métodos úteis em Dicionários

Items() dos dicionários

    Estrutura:
        itens_dicionario =dicionario.items()
    Ou então
    for item in dicionario.items()
        cada item do dicionario em formato de tuplas

-ele transforma o dicionário em tuplas
"""
vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

for produtos,qtde in vendas_tecnologia.items():
    print(f'{produtos} : {qtde} unidades') 

#Quais produtos venderam mais de 5000 unidades

#forma 1-> usando apenas o dicionario e as chaves
for chave in vendas_tecnologia:
    if vendas_tecnologia[chave]> 5000:
        print(f'{chave} :{vendas_tecnologia[chave]} unidades.')
print('---------------------------')
#forma 2-> usando o dicionario.items()

meta = 5000
for produto,unidade in vendas_tecnologia.items():
    if unidade >= meta:
        print(f'{produto} vendeu {unidade} unidade ')
        
    
