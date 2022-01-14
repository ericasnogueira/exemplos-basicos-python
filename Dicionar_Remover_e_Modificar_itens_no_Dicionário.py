"""
Dicionar,Remover e Modificar itens no Dicionário

-Estrutura:
    ºAdicionar itens:

    dicionario ={}
    dicionario[chave] = valor
outra opção:
    dicionario.upadate({chave : valor, chave : valor})

CUIDADO
obs: a forma de adicionar e modificar são a mesma maneira
"""
lucro_1tri = {'janeiro':10000, 'fevereiro':120000,'março':90000}
lucro_2tri = {'abril':88000,'maio':89000,'junho':120000}

#adicionando 1 item

print(lucro_1tri) # antes de adicionar 
lucro_1tri['abril'] = 88000
print(lucro_1tri) #depois de adicionar


#adicionando vários itens ou um dicionário a outro
lucro_1tri.update(lucro_2tri) #pode pegar pela a variavel ou coms valores ex:
#lucro_1tri.update({'abril':88000,'maio':89000,'junho':120000})
print(lucro_1tri)

#adicionando um item já existente (manualmente ou pelo update)
lucro_1tri['janeiro'] = 88000
print(lucro_1tri)

"""
    º Modificar itens:
Da mesma forma que adicionamos 1 valor, caso essa chave já exita o item é apenas modificado.
    dicionario[chave] = valor
Vamos modificar o lucro de fevereiro:
(Lembrando: caso o item não exita,ele vai criar o item no adicionário)
"""
lucro_fev = 85000
lucro_1tri['fevereiro'] = lucro_fev
print(lucro_1tri)


"""
    ºRemover itens:
        del dicionaniro[chave]
Ou então
        valor=dicionario.pop(chave)

MAS CUIDADO COM:
    del dicionario
    ->que é diferente de dicionario.clear()


OBS: se quiser so deletar mesmo usa o del, se quiser deletar mas salvar em uma variavel usa o pop    
"""

#removendo o mês de junho
del lucro_1tri['junho'] #so deletando
print(lucro_1tri)

#ex: com o pop com o mes de maio
lucro_maio = lucro_1tri.pop('maio') # deletando o mês maio mas salvando o seu valor na variavel lucro maio
print(lucro_1tri)
print(lucro_maio)


#obs: o del também fuiciona para listas, caso queira usar
#del lista[i]
funcionarios = ['João','Lira','Maria','Ana','Paula']
