#Faturamento do Melhor e do Pior mês do ano
#qual foi o valor de vendas do melhor mês do ano ? e valor do pior mês do ano ?

meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
vendas_1sem = [25000,29000,22200,17750,15870,19900]
vendas_2sem = [19850,20120,17540,15555,49051,9650]

#variavel do total de vendas
vendas_total= vendas_1sem + vendas_2sem

#adicionando vendas do 2sem no 1sem
vendas_1sem.extend(vendas_2sem)
print(vendas_1sem)


maior_venda = max(vendas_1sem)
menor_venda = min(vendas_1sem)

print(f'o maior valor é {maior_venda}')
print(f'o de menor valor é {menor_venda}')


#CONTINUAÇÃO
"""
Agora relacione as duas listas para printar 'o melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

"""

print(vendas_1sem)

i_maior = vendas_1sem.index(maior_venda)
vendas_maior=meses[i_maior]

i_menor = vendas_1sem.index(menor_venda)
vendas_menor=meses[i_menor]

#maior vendas no mes 
print(f'o melhor mês do ano foi {vendas_maior} com {maior_venda} vendas')

#menor vendas no mes
print(f'o pior mes do ano foi {vendas_menor} com {menor_venda} vendas')

"""
Calcule também o faturamento total do Ano e quanto que o melhor mês representou total.
obs: Para o faturamento total, pode usar a função sum(lista)que soma todas os itens de um lista

"""

#faturamento total
fat_total = sum(vendas_1sem)
print(f'faturamento total foi  de : R${fat_total:,}')
#percentual 
percentual = maior_venda / fat_total
print(f'O melhor mês representou {percentual:%} das vendas do ano todo')
print(f'O melhor mês representou {percentual:.1%} das vendas do ano todo')

#Crie uma lista com o top 3 valores de vendas do ano
top3 = []

print(vendas_1sem)
#vendo qual é o maior valor
maior_venda = max(vendas_1sem)
top3.append(maior_venda)#adicionando o maior valor na lista top3

vendas_1sem.remove(maior_venda)#removendo maior valor

maior_venda=max(vendas_1sem)
top3.append(maior_venda)
vendas_1sem.remove(maior_venda)

maior_venda=max(vendas_1sem)
top3.append(maior_venda)
vendas_1sem.remove(maior_venda)

print(vendas_1sem)
print(top3)
