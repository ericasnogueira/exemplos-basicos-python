#Iterando string com while




while True :
    minha_string = input("digite uma frase :")
    tamanho = len(minha_string)
    c = 0
    contagem_atual = 0
    letra = ''
    # vendo qual letra aparece mais
    while c  < tamanho :                                         
        qtd_vezes_letra = minha_string.count(minha_string[c])
                                            #para não qtd_vezes_letra com o espaço       
        if contagem_atual < qtd_vezes_letra and minha_string[c].strip() :
            letra = minha_string[c]
            contagem_atual = qtd_vezes_letra 
        
        
        c +=1 
        
    print(letra, contagem_atual)
