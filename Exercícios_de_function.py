"""
Exercícios
    Para fazer um treino simples antes de avaçarmos em mais function, vamos criar uma function que resolve
    1 "desafio simples"

1. Function para cálculo de carga tributária
(lembrando, não se atente ao funcionamento real de carga tributária, é apenas imaginário para treinarmos as
functions com algo mais prático)

-imagine que trabalha no setor contábil de uma grande empresa de varejo.

Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto,
dado o preço de venda, o "lucro" e os custos(com exceção do imposto) dele .

OBS: As  variaveis que se usa dentro da função são uma coisa e a variaveis que estão fora são outra coisa
"""
preco = 1500
custo = 400
lucro = 800

"""
Repare que o preço - custo não é igual ao lucro, porque ainda foi descontado o imposto. Sua function deve 
calcular qual foi o % de imposto aplicado sobre o preço total
"""
#function
def carga_tributaria(preco, custo, lucro) :
    imposto = preco - custo - lucro
    return imposto / preco    

#aplicação da function nos valores fornecidos para ver se ela está funcionando corretamente
print(f'A carga tibutária foi de : {carga_tributaria(preco,custo,lucro):.1%}')
