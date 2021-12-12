#listas em Python
#fatiamento
#append , insert , pop, del , clear, extend , + 
# min , max 
#range

secreto = 'perfume'
#sera salvadas nessa lista
digitadas = []
chances = 3
while True:
    letra = input ('digite uam letra:')
    if chances <= 0 :
        print('VOCÊ PERDEU !!!')
    
    if len(letra) > 1:
        print('ahhhh isso não vale, digite apenas uma letra.')
        continue
    #salvando as digitadas na lista
    digitadas.append(letra)
    
    if letra in secreto:
        print(f"UHHUHUHHHULL, a letra'{letra}' exite na palavra secreta")
    else:
        print(f"AAAFFFFFzzzz:  a letra'{letra}' NÃO EXITE NA palavra secreta.")
        #a letra incorreta não ira salvar na lista
        digitadas.pop()
        
    secreto_temporario =''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else :
            secreto_temporario += '*'
    
    if secreto_temporario ==secreto:
        print(f'Que legal VOCÊ GANHOU !!! a palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim : {secreto_temporario}')
        
    
    if letra not in secreto:
        chances -= 1
        print(f'você ainda tem {chances} chances.')
        print()
