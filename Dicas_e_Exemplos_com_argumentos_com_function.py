"""
Exemplos de parâmetros
    ° upper() -> não tem parâmetros
    ° sort() -> apenas parâmetros keyword
    ° exetend(lista) -> 1 parâmetro obrigatório
    ° nossa função eh_da_categoria(bebida,cod_categoria) ->2 parâmetros de posição obrigatórios
"""


def eh_da_categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else :
        return False

#texto para upper
cod_produto = 'beb12304'
print(cod_produto.upper())#botando as letras maisculas


#lista para sort e extend
vendas_ano = [100, 200, 50, 90, 240, 300, 55, 10, 789, 60]
vendas_novdez = [500, 1555]

vendas_ano.sort()#do menor para o maior
print(vendas_ano)

vendas_ano.sort(reverse=True) #do maior para o menor
print(vendas_ano) 

vendas_ano.extend(vendas_novdez)
print(vendas_ano)

