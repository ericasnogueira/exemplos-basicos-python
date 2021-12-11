"""
faça um programa que pergunte a hora ao 
usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
ex:
bom dia 0-11
boa tarde 12 - 17
boa noite 18-23
"""

usuario=int(input("Que horas são (0-23) ? "))

if usuario >= 0 and usuario <= 11:
    print ("Bom dia ")
elif usuario >=12 and usuario <= 17 :
    print (" Boa Tarde ")
elif usuario >=18 and usuario <= 23 :
    print (" Boa noite ")
else :
    print ('desculpa ')
