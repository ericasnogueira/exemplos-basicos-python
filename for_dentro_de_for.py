#for dentro de for 
"""
Quando temos listas dentro de listas, às vezes precisamos fazer um "for dentro de for"

for item in lista: 
    for item2 in lista2:
        codigo aqui

Vamos pegar um exemplo de nível mínimo de estoque. Em uma fábrica você tem vários produtos e não pode deixar que os produtos fiquem em falta. Para isso, foi definido uma quantidade mínima de estoque que os produtos precisam ter:

Identifique quais fábricas tem algum produto abaixo do nível de estoque

- Agora ao invés de analisar o estoque de apenas 1 fábrica, vamos analisar o estoque de várias fábricas

"""

estoque = [
    [294, 125, 269, 208, 783, 852, 259, 371, 47, 102, 386, 87, 685, 686, 697, 941, 163, 631, 7, 714, 218, 670, 453], # 0
    [648, 816, 310, 555, 992, 643, 226, 319, 501, 23, 239, 42, 372, 441, 126, 645, 927, 911, 761, 445, 974, 2, 549], # 1
    [832, 683, 784, 449, 977, 705, 198, 937, 729, 327, 339, 10, 975, 310, 95, 689, 137, 795, 211, 538, 933, 751, 522], # 2
    [837, 168, 570, 397, 53, 297, 966, 714, 72, 737, 259, 629, 625, 469, 922, 305, 782, 243, 841, 848, 372, 621, 362], # 3
    [429, 242, 53, 985, 406, 186, 198, 50, 501, 870, 781, 632, 781, 105, 644, 509, 401, 88, 961, 765, 422, 340, 654], # 4 
]    
                     # 0                1                      2                  3                 4
fabricas = ['Lira Manufacturing', 'Fábrica Hashtag', 'Python Manufaturas', 'Produções e Cia', 'Manufatura e Cia']
nivel_minimo = 50
fabrica_abaixo_nivel = []

for i,lista in enumerate(estoque) :
    #se dentro daquela lista tem alguem abaixo do nivel minimo 
    for qtde in lista:
        if qtde < nivel_minimo:
            if fabricas[i] in fabrica_abaixo_nivel :
                pass
            else:
                fabrica_abaixo_nivel.append(fabricas[i])
    
print(fabrica_abaixo_nivel)
