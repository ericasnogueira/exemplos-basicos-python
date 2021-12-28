#Formas de interromper um for
#break - interrompe e finalizar o for
#continue - interrompe e vai para o próximo item do for

vendas = [100,150,1500,2000,120]

#caso 1 - se todas as vendas forem acima da meta, a loja ganha bônus
meta1= 110

for venda in vendas :
    if venda < meta1 :
        print('loja não ganha bônus')
        break
    print(venda) # não vai aparecer por causa do break



#caso 2 - exiba quem bateu a meta 

vendedores = ['João','Julia','Ana','José','Maria']
meta = 130

for venda1 in vendas :
    if venda1 < meta :
        continue # vai pular todos abaixo da meta 
    print(venda1)# vai mostrar só os que estão acima da meta 
