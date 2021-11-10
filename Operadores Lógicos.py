#Operadores Lógicos

True or False

a=  7 != 3 and 2 >3
  
#Tabela verdade do AND

#(True and True = True 
# False and False =  False
# False and True =  False 
# False and False =  False )


# Tabela verdade do OR (ou)
# True or True = True
# True or False = True
# False or true = True                    
# False or False =  False


#Tabela verdade do XOR ('ou' exclusivo - um ou outro-)
#True != True = false
# True != False =  True 
# False != true = True
# False != False = False

#Opedaror de Negação (unário)
#not True = False
# not False = true

#CUIDADO!
#True & True
#Flase | true
#True ^ False


#BIT-A-BIT NÃO É PARA USAR QUANDO FOR USAR OPERADORES LÓGICOS 

# AND bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 10

#OR Bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 11
# 3 | 2

# XOR Bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 01
# 3 ^ 2


# Um pouco da realidade

saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo >0
despesas_controladas = salario - despesas >= 0.2 * salario

meta1 =saldo > 0 and salario - despesas >= 0.2 * salario

meta2 = saldo_positivo and despesas_controladas
