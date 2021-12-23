"""
Enumerate
 Estrutura :
 O enumerate permite que vocé percorra uma lista e ao mesmo tempo tenha em uma variável o índice daquele item.
 
 for item in lista:
     resto do código
"""
funcionarios = ['Maria','José','Antônio','João','Francisco','Ana','Luiz','Paulo','Carlos','Manoel','Pedro',
'Francisca','Marcos','Raimundo','Sebastião','Antônia','Marcelo','Jorge','Márcia','Geraldo','Adriana','Sandra',
'Luís'] 

qtd_funcionarios = 0 
for funcionario in funcionarios :
    print(funcionario)
    #pegando a quantidade de funcionarios
    qtd_funcionarios +=1
print(f'{qtd_funcionarios} funcionarios ')

"""
for i,item in enumerate(lista):
    resto do código

"""
#pegando a lista de fucionarios com o index e a quantidade
for i,funcionario in enumerate(funcionarios):
      print(f'{i} é o fucionario {funcionario}')


"""
Exemplo Prático
 Vamos pegar um exemplo de nível  mínimo de estoque. Em uma fábrica você tem vários produtos e não pode deixar que os produtos
 fiquem em falta.Par isso, foi definido uma quantidade mínima de estoque que os produtos precisam ter:

 Identifique quais produtos estão abaixo do nível mínimo de estoque.
"""
print()
estoque = [1200,300,1500,1900,2750,400,20,23,70,90,80,1100,999,900,880,870,50,1111,120,300,450,800]
produtos = ['coca','pepsi','guarana','skol','brahma','agua','del vale','dolly','red bull','cachaça','vinho tinto' 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
nivel_minimo = 50


#percorrendo a lista de estoque
#i = index
for i,qtde in enumerate(estoque):
    print(f' produto {produtos[i]} tem {qtde} em unidades')#mostrando qual o produto e o seu estoque
    #mostrar os que estão abaixo do nivel minimo
    if qtde < nivel_minimo:
        print(f'{produtos[i]} está abaixo do nível mínimo. Temos apenas {qtde} unidades')
        print()
        #print(produtos[i])#vendo qual o produto está com menos de 50
    
