"""
-Manipulando strings 
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
 Essas funções podem ser usadas diretamente em cada tipo.

"""
#positivos   [012345678]
texto      = 'python s2'
#negatiovos  [987654321]

print(texto[1])

url = 'www.google.com.br/'

#botando para não mostra a /

print(url[:-1])

#fatiamento
#pegando só o que quer 
nova_string = texto[2:6] #onde começa e onde termina
print(nova_string)
nova_string = texto[-7:-3] #com negativo
print(nova_string)

#positivos
print(texto[:1])
print(texto[:2])
print(texto[:3])
print(texto[:4])
print(texto[:5])
print(texto[:6])
#negativos
print(texto[:-4])
print(texto[:-5])
print(texto[:-6])
print(texto[:-7])
print(texto[:-8])



