"""
For 'each'
estrutura:
O for no python consegue percorrer uma lista e a cada 'loop' retornar o valor do item.

for i in range(5):
    print(i)
range(5) é na verdade uma lista do tipo : [0 , 1 , 2 , 3 , 4 ]

Usando para listas :

for item in lista:
    print(item)

ou então para string : 

for ch in texto:
    print(ch)
"""

produtos = ['coca','pepsi','guarana','sprite','fanta']
texto = 'lira@gmail.com'

tamanho = len(produtos) # pegando a quantidade de produtos

for i in range(tamanho):
    print(produtos[i])

#fazendo de outra forma 
print()#pulando uma linha
#percorrendo a lista e a cada vez que ele executa está fazendo as mesmas 5 vezes
for item in produtos:
    print(item)

#pulando linha
print()

for produtos in produtos:
    print(produtos)

print()

for ch in texto:
    print(ch)
