"""
Aplicação de Tuplas - lista de tuplas
-Estrutura :    
    Além de casos como o do enumerate, em que usamos uma função para transformar itens em tuplas
    porque isso ajuda o nosso código, temos também listas de tuplas como algo comum dentro do python

lista = [
    tupla1,
    tupla2,
    tupla3,
    ]
ou seja 

lista = [
    (valor1, valor2, valor3),
    (valor4, valor5, valor6),
    (valor7, valor8, valor9),
    ]
"""
"""
Exemplo: 
Digamos que estamos analisando as vendas do Banco de Dados de um e-commercer.
Em um determinado dia, extraiu as vendas do Banco de Dados e elas vieram nesse formato:
"""
vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

#Qual foi o faturamento de Iphone no dia 20/08/2020
faturamento = 0

for item1 in vendas :
    data, produto, cor, capacidade, unidades, valor_unitario = item1
    if produto == 'iphone x' and data == '20/08/2020':
        faturamento += unidades * valor_unitario

print(f'O faturamento de Iphone no dia 20/08/2020 foi de R$ {faturamento}')

#Qual foi o produto mais vendido(em unidades) no dia 21/08/2020 

produto_mais_vendido = ''
qtde_produto_mais_vendido = 0
cor_mais_vendido = ''
capacidade_vendido = ''
for item in vendas :
    data, produto, cor, capacidade, unidades, valor_unitario = item
    if data == '21/08/2020':
        if unidades > qtde_produto_mais_vendido:
            produto_mais_vendido = produto
            qtde_produto_mais_vendido = unidades
            cor_mais_vendido = cor
            capacidade_vendido = capacidade
print()
print(f'Meu produto mais vendido no dia 21/08/2020 foi o {produto_mais_vendido} com {qtde_produto_mais_vendido} unidades')
print()
print(f'Meu produto mais vendido no dia 21/08/2020 foi o {produto_mais_vendido} com {qtde_produto_mais_vendido} unidades.Cor : {cor_mais_vendido}, capacidade {capacidade_vendido}')
