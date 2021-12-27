"""
Exercícios

## 1. Calculando % de uma lista

Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso,
 mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.

Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, 
eu quero conseguir calcular o % de vendedores que bateram a meta.
Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.


"""

meta = 10000
vendas = [
    #   0      1       
    ['João', 15000], # 1 
    ['Julia', 27000],# 2 
    ['Marcus', 9900],# 3
    ['Maria', 3750], # 4 
    ['Ana', 10300],  # 5
    ['Alon', 7870],  # 6
]

#- Vamos resolver de 2 formas:
 #   1. Criando uma lista auxiliar apenas com os vendedores que bateram a meta

#criando lista auxiliar 
acima_meta = []

for venda in vendas : 
    if venda[1] >= meta:
        acima_meta.append(venda)
print(acima_meta)
print(f'{len(acima_meta) / len(vendas):.0%} dos vendedores bateram a meta .')

print()#pulando linha 

#  2. Fazendo o cálculo diretamente na lista que já temos

qtde_vendedores_acima = 0

for venda1 in vendas:
    if venda1[1] >= meta:
        qtde_vendedores_acima = qtde_vendedores_acima + 1 #qtde_vendedores_acima += 1 

print(f'{ qtde_vendedores_acima / len(vendas):.0%} dos vendedores bateram a meta .')


#crie um código para responder: quem foi o vendedor que mais vendeu?

melhor_vendedor = ' '
maior_venda = 0

for venda2 in vendas:
    if venda2[1] > maior_venda:
        maior_venda = venda2[1]
        melhor_vendedor = venda2[0]
print(f' o  melhor vendedor foi {melhor_vendedor} com {maior_venda}')
