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
