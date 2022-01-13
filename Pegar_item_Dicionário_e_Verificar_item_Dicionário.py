"""
Não confie na ordem dos dicionários, use as chaves

Python Versões Antigas x Versões Novas
    º Dicionários eram 'sem ordem'. Atualmente tem ordem, mas certo é usar as chaves
    º 2 formas de pegar um valor:
        º dicionário[chave]
        º .get(chave)



"""
mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

"""
º Qual foi o item mais vendido nas categorias 'livros' e 'lazer'?
º Quanto foi vendido de 'notebook asus' e de 'ipad' ? 
"""
#Respondendo com a chave
print(f'O livro mais vendido foi {mais_vendidos["livros"]}')#tem que ser com aspas duplas
print(f'O produto mais vendido em lazer foi {mais_vendidos["lazer"]}')

#Respondendo com o método get

print(f'O notebook asus vendeu {vendas_tecnologia.get("notebook asus")}') #so vai com aspas duplas
print(f'Vendemos {vendas_tecnologia.get("ipad")} ipads')


"""
Verificar se item está no dicionário :
    º if
    º .get(chave)=None

EX:
Se tentarmos procurar as vendas de 'copo' na lista de vendas tecnologia, o que acontece ?
"""

if 'copo' in vendas_tecnologia:
    print(vendas_tecnologia["copo"])
else :
    print('Copo não está dentro da lista de produtos de tecnologia')


if vendas_tecnologia.get("copo") == None:
    print('Copo não está dentro da lista de produtos de tecnologia 22200')
else:
    print(vendas_tecnologia.get("copo"))
