"""
Estrutura While : 
Usamos o while quando queremos repetir um código de forma indeterminada até uma condição se tornar verdadeira/falsa.
A lógica é : enquanto a condição for verdadeira, o while executa o código, assim que ela terminar de ser verdadeira,o código 
"sai" do while.

while condicao:
    repete esse código

º exemplo : quando criamos automações na internet.
º exemplo2 : crie um programa que funcione como registro de vendas de uma empresa.
Nele, a pessoa deve inserir o nome do produto e o produto deve ser adicionando na lista de vendas.Enquanto o usuário não encerrar 
o programa, significa que ele está registrando novos produtos, então o programa deve permitir e entrada de quantos produtos o
usuário quiser.
"""

venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia:  ')
vendas = []

#variavel venda diferente de vazio 
while venda != '' : 
    vendas.append(venda)
    venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia:  ')


print(f'Registro Finalizado. Os produtos cadastros fora : {vendas}')
