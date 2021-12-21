#Lista de Listas 
"""
Cada item de uma lista pode ser qualquer tipo de variavel.Inclusive, uma lista.
Quando dentro de uma lista temos cada item como sendo uma outra lista, temos uma "nested list", ou seja uma lista de listas.

"""
             #  0      1      2        3 
vendedores = ['Lira','João','Diego','Alon']
            # 0        1
produtos = ['ipad','iphone']
vendas = [
   #  0   1  
    [100,200], #lira   0
    [300,500], #joao   1 
    [50,1000], #diego  2 
    [900,10],  #alon   3
] 

print(vendas)
#quanto João vendeu de ipad ?
vendas_ipad_joao = vendas[1][0]
print(vendas_ipad_joao)
print()
#quanto diego vendeu de iphone ? 
vendas_iphone_diego = vendas[2][1]
print(vendas_iphone_diego)
print()
#total de vendas de iphone ?
vendas_iphone = vendas[0][1]+ vendas[1][1]+ vendas [2][1] + vendas[3][1]
print(vendas_iphone)

#e se lira na verdade fez apenas 50 vendas de Iphone, como modifico na minha lista o valor de vendas dele ? 

vendas [0][1] = 50
print(vendas)

# e se agora eu tenho um novo produto 'mac', como adiciono as vendas em cada um dos vendedores ? 
#             0    1    2    3  
vendas_mac = [10 , 15 , 6 , 70]

   
vendas [0].append(vendas_mac[0])
vendas [1].append(vendas_mac[1])
vendas [2].append(vendas_mac[2])
vendas [3].append(vendas_mac[3])

print(vendas)
