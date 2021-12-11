"""
faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

usuario =input('Digite um número inteiro : ')

#isdigit esta perguntado se so tem numeros 
if usuario.isdigit():
    usuario =int(usuario)
    
    if usuario % 2 == 1:
        print ('o número é impar ')
    else:
        print('o número é par')
else:
    print('não é número inteiro')


