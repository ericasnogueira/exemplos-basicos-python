"""
índices em lista, consultando e modificando os valores

"""
produto = ['tv','celular','mouse','teclado','tablet']
vendas = [1000, 1500 , 350, 270, 900]

#pegando o índice de produto e de vendas 
print(f'vendas do produto {produto[1]} foram de {vendas[1]} unidades.')

#modificando um valor de vendas 
vendas [3]=300

print(f'vendas do produto {produto[3]} foram de {vendas[3]} unidades.')

#modificando uma string  #atribuindo um novo valor 
texto = 'lira@gmail.com'
texto = texto.replace('i','a') #aqui ira substituindo os dois i 
print(texto)

