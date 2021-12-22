"""
Estrutura de Repetição  : for
 funcionamento : 
 for i in range(n):
     repetir código n vezes
"""

for i in range(5): # 0 1 2 3 4
    print('lira ')

#Imagine que você está construindo uma automação para enviar todo dia por e-mail um resumo da produção de uma fábrica.
#Construa um código que exiba quantidade produzida de cada os produtos nesse 'e-mail'
          #   0       1       2           3     4 
produtos = ['coca','pepsi','guarana','sprite','fanta']
producao = [15000,12000,13000,5000,250]
          #   0    1     2      3    4
  
tamanho = len(produtos)#pegando a quantidade que tem na lista 
print(tamanho)


# i = 0 (por onde começa)
#tamanho 
for i in range(tamanho):
    print(f'{produtos[i]} unidades produzidas de {producao[i]}')
