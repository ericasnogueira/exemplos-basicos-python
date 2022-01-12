"""
Dicionários em Python
-Estrutura :
    dicionario = {chave:valor,chaver:valor,chave:valor,chave:valor...}

Vantagens e Desvantagens 
º Não devem ser usados para pegar itens em uma determinada ordem
º Podem ter valores heterogêneos(varios tipos de valores dentro de um mesmo dicionario:inteiros,strings,listas,etc)
º Chaves são unicas obrigatoriamente
º Mais intuitivos de trabalhar
"""
mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

#Qual foi o item mais vendido nas categorias 'livros' e 'lazer' ?

#no dicionario não precisa botar o indice
livro = mais_vendidos['livros']
lazer = mais_vendidos['lazer']

print(f'O livro mais vendido foi : {livro}')
print(f'O item mais vendido na categoria lazer foi : {lazer}')


#Quando foi vendido o 'notebook asus' e de 'ipad'?
qtde_noteasus = vendas_tecnologia['notebook asus']
qtde_ipad = vendas_tecnologia['ipad']

print(f'Foi vendido {qtde_noteasus} do notebook asus')
print(f'foi vendido {qtde_ipad} do ipad ')
