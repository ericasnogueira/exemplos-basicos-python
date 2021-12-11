#Pass e Ellipsis como placeholders

#Pass é usado quando o progrmador ainda não sabe 
# o que botar aqui para que não gere erro

valor1 = False #pode ser True tambem so que não ia aparecer nada 

if valor1 :
    pass
else :
    print('foi')
    
    
#Ellipsis - mesma coisa que o pass  no contexto
#segurando o lugar


valor2 = False

if valor2 :
    ...
else:
    print('foi2')
