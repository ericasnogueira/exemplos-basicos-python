#Alterações'incrementais' de variáveis

#estrutura
 #variável = variavel * outro_valor
#ou então
 #variavel *=outro_valor


faturamento = 3000
faturamento = faturamento + 1000

email='lira@gmail'
email = email + '.com'
print(faturamento)
print(email)

lista = ['mac', 'iphone']
vendas = [100,200]

lista.append('ipad')#adicionando ipad na lista 

#pode adicionar assim tambem
#lista = lista + ['ipad2']
print(lista)

soma_vendas = 300
#adicionando na soma a quantidade de ipad
soma_vendas = soma_vendas + 500
print(soma_vendas)

email2= f'Esse mês vendemos um total {soma_vendas} produtos, sendo :\n{vendas[0]} unidades de {lista[0]}\n{vendas[1]} unidades de {lista[1]}'
#adicionando no fim do texto o ipad
#500 são do ipad
email2 += f'\n{500} unidades de ipad '

print(email2)
