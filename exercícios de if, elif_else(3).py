#exercícios de comandos condicionais
"""
Leia um numero fornecido pelo usu ´ ario. Se esse n ´ umero for positivo, calcule a raiz ´
quadrada do numero. Se o n ´ umero for negativo, mostre uma mensagem dizendo que o ´
numero ´ e inv ´ alido.
"""

nu1=int(input('digite um numero : '))

if nu1 > 0:
    raiz = nu1 /2
    print(f'a raiz quadrada de {nu1} é {raiz} ')
else : 
    print(' número inválido')


