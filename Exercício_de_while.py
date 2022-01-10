"""
Exercícios
1- Input até o usuário parar

vamos criar um sistema de vendas. Nosso programa deve registrar os produtos e as quantidades(2 input) e adicionar em uma lista.
O programa deve continuar rodando até o input ser vazio, ou seja, o usuário apertar enter sem digitar nenhum produto ou quantidade.
Ao final do programa, ele deve printar todos os produtos e quantidades vendidas.

obs: Caso queira,para print ficar mais visual, pode usar o join para cada item ser printado em uma linha.Sugestão para sua lista 
de produtos vendidios;

"""
vendas = [
     # 0    # 1
    ['maçã', 5], # 0
    ['banana', 15], #1
    ['azeite', 1], #2
    ['vinho', 3], #3
]
vendas1 = []



while True : #rodando infinitamente
    produto = input('Qual o produto ? : ')
    if not produto :  # se não tiver preenchido o codigo ira parar
        break
    qtde = int(input('Qual a quantidade ? :'))
    vendas1.append([produto , qtde])
print(vendas1)
    
    
