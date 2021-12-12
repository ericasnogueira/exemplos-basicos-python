#listas em Python
#fatiamento
#append , insert , pop, del , clear, extend , + 
# min , max 
#range


l1 = [1,2,3] #lista 1
l2 = [4,5,6] #lista 2
l3 = l1 + l2 #lista 3

#adicionando valores nas listas
l1.extend(l2)# pegando os valores de lista 2
l1.extend('er')

#adcionando so UM valor
l1.append('erica')
l1.append('silva')

print(l1[-1])

#adicionando em qualquer lugar na lista
l2.insert(0,'banana')

print(l1)
print(l2)
print(l3)

