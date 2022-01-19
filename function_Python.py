"""
Function Python

o que é ?
    As functions são blocos de códigos que servem 1 único propósito, fazem uma ação espécifica.

    -Estrutura Básica:
    def nome_funcao():
        faça alguma coisa 
        faça outra coisa
        return valor_final

"""
#Exemplo: vamos criar uma função de cadastro de um produto.Essa função deve garantir que produto cadastro 
#está em letra minúscula.
"""
produto = input('Digite o nome do produto que deseja cadastrar :')

#transformando tudo em letra minuscula
produto = produto.casefold()

print(f'Produto {produto} cadastradado com sucesso')
"""

#botando dentro de uma função

def cadastrar_produto():
    print('-' *15)
    produto1 = input('Digite o nome do produto que deseja cadastrar :')
    produto1 = produto1.casefold()
    print(f'Produto {produto1} cadastradado com sucesso')
    print('-' *15)

for i in range(3):   #cadastrando 3 produtos
    cadastrar_produto() #chamando a função
