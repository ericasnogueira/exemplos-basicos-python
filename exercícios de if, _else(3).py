"""
faça um programa que peça o primeiro nome do usuário. se o nome tiver 4 letras ou
menos  escreva 'seu nome é curto'; se tiver entre 5 e 6 letras, escreva 
'seu nome é normal'; maior que 6 escreva 'seu nome é muito grande'
"""

usuario = input('digite seu nome :')
qtd_nome= len(usuario)



#chamo essa variavel
if qtd_nome <=4:
    print ('seu nome é curto')
elif qtd_nome >=5 and qtd_nome <= 6 :
    print ('seu nome é normal')
elif qtd_nome > 6 :
    print ('seu nome é muito grande')
else:
    print()
