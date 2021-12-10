#Operadores lógicos if_elif_else
#and  (as duas comparações precisa ser verdadeira)
# or (uma das duas expressões precisa ser verdadeira)
# not ()
#  in e not in 

#verdadeiro  E verdadeiro
#comparacao1 and comparacao2

#verdadeiro OU verdadeiro
#comp1 or comp2

#not

a=2
b=3

#se não (inverte a situação)
if not b > a:
    print('b é maior que a')
else:
    print('a e maior que b')
    
    
nome = 'erica'
#perguntando se a letra em questão estão na variavel
#se 'i' esta na variavel 'nome' faça  o comando if
if 'i' in nome:
    print('exite  ')
else :
    print("nao")
    
#se  'oq tiver aqui' NAO ESTIVER na variavel nome faça o comando if 
if 'asdas' not in nome :
     print('nao ')
else :
    print("exite")
    
