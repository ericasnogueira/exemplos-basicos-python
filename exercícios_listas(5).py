"""
1-Mudança de Carga Tributária
 ºReformas e mudanças de cargas tributárias são bem comuns no Brasil.
- você trabalha em uma empresa de ecommerce
No brasil, o imposto sobre livros é zerado. De um ano para outro, o governo criou um novo imposto que indice em 10% sobre o valor dos 
livros e agora você precisa alterar o registro dos preços dos livros da empresa para garantir que esse imposto vai ser repassado para 
o preço final do produto.
Crie um código que recalcule o valor do livro da sua lista de produtos e ajuste na tabela.
Além disso,calcule qual vai ser o impacto financeiro da criação desse imposto para a empresa (ou seja, quanto que o imposto vai aumentar 
de custo para a empresa)
obs: para facilitar, colocamos apenas 1 livro na lista, mas em breve vamos aprender um for que vai adaptar esse cenário para qualquer 
quantidade de livros na sua lista.
obs2:seu código deve funcionar mesmo que haja livros na lista de produtos da empresa.

"""
#             0             1      2         3      4             5         6       7                  8
produtos = ['computador','livro','table','celular','tv','ar condicionado','alexa','máquina de café','kindle']

#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    #  0     1 
    [10000, 2500], #0
    [50000, 40],   #1 livro
    [7000, 1200],  #2
    [20000, 1500], #3
    [5800, 1300],  #4
    [7200, 2500],  #5
    [200, 800],    #6
    [3300, 700],   #7
    [1900, 400]    #8
]
# se tiver livro no produtos
if 'livro' in produtos :
    i_livro = produtos.index('livro') #pegando o index do livro
    total_antigo = produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
    produtos_ecommerce[i_livro][1] = produtos_ecommerce[i_livro][1] * 1.1
    novo_total = produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
    print(f'Vamos pagar de imposto a mais : R${novo_total - total_antigo:,}')
