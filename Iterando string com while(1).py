#Iterando string com while


minha_string = 'o rato roeu a roupa do rei de roma'

print(minha_string.count('a'))#perguntando quantas vezes a letra aparece

tamanho = len(minha_string)

c = 0
nova_string = ''
while c  < tamanho :

    if minha_string[c]=='r':
        nova_string = nova_string + minha_string[c].upper()#botando para que todos os r sejam maiusculos
    else :
        nova_string = nova_string + minha_string[c]
    #print(c, minha_string[c])
    #print(nova_string) # montando a frase linha por linha
    
    c+=1
    #não vai aparecer r na frase
print(nova_string)
