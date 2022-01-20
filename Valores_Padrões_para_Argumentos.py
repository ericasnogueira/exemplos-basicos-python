"""
Valores Padrões para Argumentos
    Estrutura:
    ° Nesse caso, não é obrigado a passar o valor para usar a função, pode usar o valor padrão

    def minha_funcao(argumento = valor_padrao):
        ...
        return ...
° Como vimos, o sort() para listas tem argumentos padrão. O reverse = False é padrão, então a ordem 
é crescente. Caso o usuário queira fazer em ordem descrescente, o reverse deve ser alterado para true 
"""

produtos = ['apple tv', 'mac' , 'iphone x', 'ipad', 'apple warch', 'mac book', 'airpods']

produtos.sort()
print(produtos)

produtos.sort(reverse= True)
print(produtos)

"""
° Vamos criar uma função que padronize códigos de produtos. O default será padronizar os  códigos para letras 
minúsculas(dado por 'm'), mas se o usuário quiser pode padronizar para maiúscula, dado por ('M').
"""
def padronizar_codigos(lista_codigos, padrão = "m"):
    #seu código aqui
    for i,item in enumerate(lista_codigos):
        item = item.replace('  ', ' ')
        item = item.strip()
        if padrão == 'm':
            item = item.casefold()
        elif padrão == 'M':
            item = item.upper()
        lista_codigos[i] = item
    return lista_codigos

cod_produtos = ['ABC12', 'abc34', 'AbC37']
print(padronizar_codigos(cod_produtos, "m")) #tudo minusculo
print(padronizar_codigos(cod_produtos, "M"))# tudo maisculo
