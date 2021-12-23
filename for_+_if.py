"""
for  + if 

Estrutura :
 for item in lista:
     if condição :
         faça alguma coisa
    else :
        outra coisa

Digamos que esteja analisando a meta de vendas de vários funcionários de uma empresa. A meta de vendas é de 1000 reais em 1 dia.
temos uma lista com vendas de todos os funcionários e quero calcular qual o % de pessoas que bateram a meta.
"""
vendas = [1200,300,800,1500,1900,2750,400,20,23,70,90,80,1100,999,900,880,870,50,1111,120,300,450,800]
meta = 1000

#quantidade de funcionarios
tamanho_vendas= len(vendas)

for venda in vendas:
    print(venda)
print()



qtde_bateu_meta = 0 
#mostrar só as vendas que bateram a meta 
for venda_metas in vendas :
    if venda_metas >= meta:
        #mostrando o número de vendas
        print(venda_metas)
        # pegando a quantidade que bateu a meta 
        #qtde_bateu_meta = qtde_bateu_meta + 1 
        qtde_bateu_meta += 1 #simplificando o de cima 
print(f'só {qtde_bateu_meta} bateram a meta ')

print(f'O percentual de pessoas que bateram a meta foi de {qtde_bateu_meta / tamanho_vendas:.1%}')
