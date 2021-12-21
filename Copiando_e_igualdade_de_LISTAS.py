#Copiar e "Igualdade" de listas
"""
Estrutura :
- Quando fazemos:
  lista2 = lista1
  não estamos criando uma lista nova, mas estamos atribuindo outra variável à mesma lista.
- Se quisemos copiar lista devemos fazer :
  lista2 = lista1.copy()
  ou então
  lista2 = lista1[:]
"""
lista = ['ipad','iphone x ','apple tv']
lista2 = lista 

lista[1] = 'iphone 11' #modificando valor

print(lista)
print(lista2)

#copiando 

lista3 = ['ipad','iphone x ','apple tv']
lista4 = lista3.copy()
lista5 = lista3[0]#copiando um item especifico pelo indice 
lista6 = lista3[:1]



lista3[1]= 'iphone 11'
print(lista3)
print(lista4)
print(lista5)
print(lista6)
