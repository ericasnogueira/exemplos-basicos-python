#Juntar Listas, Ordenar e Cuidados Especiais
#lista1.extend(lista2)
#lista_nova = lista1 + lista2

#obs: o método .append não junta listas, mas adiciona um valor no final da lista

#CUIDADO : 
#[1] + [2] não é a mesma coisa que 1 + 2, então cuidado sempre com o formato dos valores na hora de fazer operações.



produtos =['apple tv','mac','iphone x','iphone 11','Ipad','apple watch','macbook','airpods']
novos_produtos = ['iphone 12', 'iphone 13']

produtos.extend(novos_produtos) #produtos ira adicionar novos produtos 
print(produtos)
print()

#ira adicionar duas vezes novos produtos pq produtos ja adicionou anteriormente eles  
todos_produtos = produtos + novos_produtos
print(todos_produtos)
print()

#cuidado
#fica como uma lista dentro de outra lista
produtos.append(novos_produtos)
print(produtos)
print()

vendas = [1000,1500,15000,20000,270,900,100,1200]
vendas_iphonex = [15000]
vendas_iphone11 = [20000]

#quero saber o total de vendas de iphone (só da lista de vendas (tem que ser pelo indice deles ) )
total_iphone = vendas[2] + vendas[3]
print(total_iphone)

total_iphone_listas = vendas_iphonex + vendas_iphone11 #vai aparecer os dois valores não a soma deles 
print(total_iphone_listas)

#só ira pelo indice deles que é 0 
total_iphone_listas2= vendas_iphonex[0] + vendas_iphone11[0]
print(total_iphone_listas2)



#ORDENAR LISTAS 
#list.sort()
#nomedalista.sort
#python reconhecer letras maiúsculas primeiro que letras minúsculas
#ordem da tabelas ASCII
produtos_ordee =['apple tv','mac','iphone x','iphone 11','Ipad','apple watch','macbook','airpods']

produtos_ordee.sort()
print(produtos_ordee)

vendas.sort()
print(vendas)

#do maior para o menor
vendas.sort(reverse=True)
print(vendas)
