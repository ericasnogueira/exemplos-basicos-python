"""
Adicionar e Remover itens da lista

"""

#exemplo          0          1          2        3       4           5         6        7
produtos1 = ['produtos 1','apple tv','mac','iphone x','Ipad','apple watch','macbook','airpods']
print(produtos1)

#produtos para testes

produtos = ['produtos','apple tv','mac','iphone x','Ipad','apple watch','macbook','airpods']
print(produtos)

#trocando algo da lista pelo índice 
produtos[3] = 'iphone 11'
print(produtos)

#adicionar o  iphone 11
produtos1.append('iphone 11')
print(produtos1)

#removendo o iphone 11 
#são duas formas
#removendo pelo o nome 
produtos1.remove('iphone x')
print(produtos1)

#removendo pelo índice
produtos1.pop(7) # removendo o iphone 11 que tinha adicionado
print(produtos1)

#removendo o iphone trocado mas salvando na variavel para mostra qual foi trocado
item_removido = produtos.pop(3)
print(produtos)
#mostrando qual foi removido 
print(f'o item removido de produtos foi {item_removido}.')
