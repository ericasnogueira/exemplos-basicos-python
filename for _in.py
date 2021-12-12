"""
for in em python
Iterando strings com for
Função range(start= 0 , stop , step =1)

"""
# continue - pula para o proximo laço
# break - termina o laço

texto = 'Python'

#para 'letra' em texto mostre
for letra in texto:
    print (letra)
    
    
for n in range(10):
    print (n)
    
print('###############')

for n in range (100):
    if n % 8 == 0:
        print(n)
        
print('###############')


for n in range (0,100,8):
        print(n)
        
print('###############')
print('###############')
#botando as letras t e h maiusculas  com for

nova_string =''

for letra in texto :
    if letra == 't':
        nova_string += letra.upper() #nova_string = nova_string + letra.upper 
    elif letra == 'h':                
        nova_string += letra.upper()  #pode ser desses dois meios
    else :
        nova_string += letra
print(nova_string)
        
