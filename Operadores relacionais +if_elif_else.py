#Operadores Relacionais 
# == igualdade 
# > mair que  
# >= maior que ou igual a 
# < menor que 
# <= menor que ou igual a 
# != diferente 

#Queremos um emprestimo mas so sera liberado se for maior de 18

#primeiro modo
print("primeiro")
nome=input("qual é o seu nome ?")
idade=int(input("qual é a sua idade ?"))

if idade >= 18 :
      print('emprestimo liberado')
else :
      print('emprestimo negado')

print()
#segundo modo 
print('segundo')
nome2 = input("qual é o seu nome ?")
idade2 = input("qual a sua idade ?")

idade2 = int(idade2)

#limite para pegar emprestimo
idade_limite = 18

if idade2 >= idade_limite:
      print(f'{nome2} pode pegar o emprestimo.')
else :
      print(f'{nome2} não pode pegar o emprestimo')
      
print()
# entra 20 e 30 anos 

print('terceiro')
nome3 = input("qual é o seu nome ?")
idade3 = input("qual a sua idade ?")

idade3 = int(idade3)

#limite para pegar emprestimo
idade_menor = 20 #jovem
idade_maior= 30 #passou da idade

if idade3 >= idade_menor and idade3 <= idade_maior:
      print(f'{nome3} pode pegar o emprestimo.')
else :
      print(f'{nome3} não pode pegar o emprestimo')
      
