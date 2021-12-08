#Input Entrada de dados do usuario 
#Entrada de dados              

#mesmo botando alguma coisa que não seja
#string sempre ira retorna ela (string)
nome = input("Qual e o seu nome ? ")
print(f'O usuario digitou {nome} e tipo da variavel e 'f'{type(nome)}')


print()#quebrando uma linha

idade = input("Qual e a sua idade? ")
print(f'O usuario {nome} tem a idade {idade} ')

print()
                    #convertendo uma string para um int  
ano_nascimento = 2021 -int(idade)

print(f'{nome} tem {idade} anos.'                   
      f' {nome} nasceu em {ano_nascimento}.')


#outro exemplo 
#calculadora so faz soma

#tem que ter  esse int pq se nao tiver ira concatenar 
#ficaria 15 + 15 = 1515
#sem o int ficaria com str então convertemos a entrada de str para int

a = int(input('primeiro numero : '))
b= int(input('segundo numero : '))

c = a + b 
print(f'{a} + {b} = {c}')
#so mostrando o resultado
print(a + b) #soma
print(a * b) #multiplicação
print(a / b) #divisçao


