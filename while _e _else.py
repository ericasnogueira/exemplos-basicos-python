##while e else

contador = 1
acumulador =1

while contador <= 10:
    print (contador, acumulador)
    
    acumulador = acumulador + contador
    contador +=1
    
    
contador1 = 1
acumulador1 =1

while contador1 <= 10:
    print (contador1, acumulador1)
    
    if contador1 >5:
        break
    
    acumulador1 = acumulador1 + contador1
    contador1 +=1
#não precisado if aqui
else :
    print ('cheguei no else') #não vai ser executado por conta do break
print ('isso sera executado.')

    

    

    

