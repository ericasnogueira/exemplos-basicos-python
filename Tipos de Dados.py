#TIPOS DE DADOS
"""
str - string = textos - 'Assim'  "Assim"
int - inteiro - 123456 0 - 10 - 20 - 500 - 15000
float - real/ponto flutuante - 10.50 1.5 -10.90 16.3 0.0 
bool - booleano/lógico = true / false 10==10
"""

#retornando as classes
print('luiz', type('luiz'))#str
print('10', type('10'))#str, não é int por causa das a ''
print(10, type(10))#int
print(25.23, type(25.23))#float

#booleano não precisa ser só números
print(10==10, type(10==10))#true
print('l'=='l', type('l'=='l'))#true
print('l'=='L', type('l'=='L'))#false


#convertindo um tipo para outro

print('luiz',type('luiz'),bool('luiz'))#str -> bool 
print('10',type('10'),type (int('10')))#str -> int

print('erica', type('erica'))#Nome
print(20, type(20))#idade
print(1.64, type(1.64))#altura
print(20>=18, type(20>=18))#maior de idade

