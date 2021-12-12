#listas em Python
#fatiamento
#append , insert , pop, del , clear, extend , + 
# min , max 
#range


l1 = [1,2,3] #lista 1
l2 = [4,5,6] #lista 2
l3 = l1 + l2 #lista 3

 #    0 1 2 3 4 5 6 7 8
l4 = [1,2,3,4,5,6,7,8,9]#lista 4
print(l2)
l2.insert(0,'banana')
print(l2)

#deletando um no final da lista
l2.pop()
print(l2)
 
#deletando qual queremos deleta da listas
del(l4[3:5])
print(l4)
del(l2[0])
print(l2)

#pegando o valor max e min

print(max(l4))
print(min(l4))

l5= [0,1,2,3,4,5,6,7,8,9]

