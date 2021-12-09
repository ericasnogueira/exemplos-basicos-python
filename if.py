

#se
if False:
      print('VERDADEIRO.')
#se não 
elif  False:
      print(' AGORA É VERDADEIRO.')
elif False:
      print("MAIS UMA VERDADEIRA.")
#senão
else : 
      print("NÃO É VERDADEIRA")
      
#outro jeito

if False:
      print('VERDADEIRO.')
      print('teste teste 2')
      
elif  True:
      print(' AGORA É VERDADEIRO')
      nome = input('QUAL É O SEU NOME ?')
      
      print(f'seu nome é {nome}')
      
elif False:
      print("MAIS UMA VERDADEIRA.")
      print(22+22)

else : 
      print("NÃO É VERDADEIRA")
      print('ola')





car ='Audi'
car2 ='AUDI'


#normal
if car2 == "AUDI" :
  print("certo A")

#lower => ignora as letras maiusculas e minusculas   
  
  
#lower não aceitas todas as letras so a primeira
if car.lower() == 'AUDI':
    print("certo B ")

#aceita todas as letras minusculas
if car2.lower() == 'audi':
      print("certo C")

#aceita todas letras 
if car.lower() == "audi" :
    print('certo D ')

#noraml
if car =='Audi':
    print("certo E")
