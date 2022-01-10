"""
Loop Infinito no While

(cuidade com while -> Loop Infinito)
Sempre que for usar o comando while, lembre-se de ter certeza que o programa vai terminar em algum momento.

exemplo:
Digamos que tempos um lista de vendedores e as quantidade vendidas e queremos identificar todos os vendedores que bateram a 
meta de 50 vendas

"""

vendas = [941,852,714,697,686,685,670,631,453,386,371,294,269,259,208,163,125,102,87,47,7]
vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 
'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
meta = 50

#indice
i = 0 

while vendas[i] > meta :
    print(f'{vendedores[i]} bateu a meta. vendas :  {vendas[i]}')
    i = i + 1 #para não da o loop e passar para o proximo ( i += 1)
