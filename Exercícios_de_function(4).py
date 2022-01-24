"""
Exercícios

1- Cálculo do percentual e da lista de vendedores
°   Queremos criar uma function que consiga identificar os vendedores que bateram uma meta,mas além disso,
    consigo já me dar como resposta o cálculo do % da lista de vendedores que bateu a meta(para que eu não 
     precisar calcular manualmente depois)

°    Essa function deve receber 2 informações como parâmetro: a meta e um dicionário com os vendedores e suas
    vendas. E me dar 2 respostas : uma lista com o nome dos vendedores que bateram a meta e o % de vendedores
    que bateu a meta.
"""
meta = 10000
vendas = {
    'João' : 15000,
    'Julia' : 27000,
    'Marcus' : 9900,
    'Maria' : 3750,
    'Ana' : 10300,
    'Alon' : 7870,
}  
#Function
def calculo_meta(meta, vendas):
    #lista de quem bateu
    bateram_meta = []

    #percorrendo a lista de vendedoes
    for vendedor in vendas :
        #bateu a meta ?
        if vendas [vendedor] >= meta: #acessando o valor 
            bateram_meta.append(vendedor)#adicionando quem bateu
    perc_baterammeta = len(bateram_meta) / len(vendas)
    return perc_baterammeta, bateram_meta

#aplicação da function 
p_meta, vendedores_acima_meta = calculo_meta(meta, vendas)
print(p_meta)
print(vendedores_acima_meta)

print(calculo_meta(meta,vendas))
