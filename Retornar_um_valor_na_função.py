"""
Retornar um valor na Function Python

    Estrutura Básica:
        def nome_funcao():
            return valor_final
"""
#Exemplo: vamos criar uma função de cadastro de um produto. Essa função deve garantir que o
#produto cadastrado está com letra minúscula.

"""
OBS: qualquer variavel que exite dentro de uma função só exite nela 
"""


def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadatrar :')
    produto = produto.casefold() # botando as letras minusculas
    produto = produto.strip() #removendo o espaço extra no inicio e no final da palavra 
    print(f'Produto {produto} cadastrado com sucesso')
    return produto



                     #chamando a função
produto = cadastrar_produto() 


# só assim que vai mostrar o produto que foi cadastrado
print(produto) 

