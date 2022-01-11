"""
Tuplas
Estrutua : 
    tupla = (valor,valor,valor,...)
Diferença:
    Parece uma lista, mas é imutável
Vantagens:
    º Mais eficiente(em termos de performance)
    º Protege a base de dados (por ser imutável)
    º Muito usado para dados heterogêneos
"""
#Criando tuplas 
          #  0        1          2           3      4 
vendas = ('lira','25/08/2020','15/02/1994',2000,'Estagiário')

#Acessando o valor de uma tupla
# 1º jeito
nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]

#2º jeito

#em ordem da tup
nome1,data_contratacao1,data_nascimento1,salario1,cargo1 = vendas # de acordo com a quantidade de valores que tem na tupla

#mostrando do 1º jeito
print(nome)
print(data_contratacao)
print(data_nascimento)
print(salario)
print(cargo)

print()#pulando uma linha

#mostrando do 2º jeito

print(nome1)
print(data_contratacao1)
print(data_nascimento1)
print(salario1)
print(cargo1)

#pulando uma linha
print()

#Enumerate que vinhamos usando até agora, na verdade, cria uma tupla para a gente.

vendas1 = [1000,2000,300,300,150]
funcinarios = ['João','Lira','Ana','Maria','Paula']

for i, venda in enumerate(vendas1):
    print(f'{funcinarios[i]} vendeu {venda} unidades')
