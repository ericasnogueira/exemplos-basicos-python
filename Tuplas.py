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

nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]

print(nome)
print(data_contratacao)
print(data_nascimento)
print(salario)
print(cargo)
