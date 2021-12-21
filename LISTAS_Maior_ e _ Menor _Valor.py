#Maior e Menor Valor 

produtos =['apple tv','mac','iphone x','Ipad','apple watch','macbook','airpods']

#Quantos produtos temos a venda ?

tamanho  = len(produtos)
print(f'temos {tamanho} produtos ')

"""
Maior e Menor Valor 

maior = max(lista)
menor = min(lista)
"""
vendas = [1000,1500,15000,270,900,100,1200]

#qual o item mais vendido ?
#qual o item menso vendido?

mais_vendido = max(vendas)
menos_vendido = min(vendas)

print(f'O produto mais vendido teve {mais_vendido} unidades e o menos vendido teve {menos_vendido} unidades vendidas')
print()

#vai da a posição do produto mais vendido - pelo o  indice

i =vendas.index(mais_vendido)
produto_mais_vendido = produtos[i]

print(f'o produto mais vendido foi {produto_mais_vendido} com {mais_vendido} unidade vendidas')
print()


a = vendas.index(menos_vendido)
produto_menos_vendas = produtos[a]
print(f'o produto com menos vendas foi {produto_menos_vendas} com {menos_vendido} unidade vendidas')

