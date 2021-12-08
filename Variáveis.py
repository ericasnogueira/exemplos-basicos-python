#Variáveis
a = 10
b = 5.2

print(a + b)

a = 'agora sou uma string'
print(a )
print(b) 

#print(a + b) -> não ira pq a mão é mais 10 e sim uma string  



#comentários
 
salario = 3450.45
despesas = 2456.2 
saldo = salario - despesas
print( saldo)
print('meus salario e : ' ,salario)
print('minhas contas sao : ', despesas)
print('vou ficar com : ' ,saldo)
print('fim de verdade ')

""""
asddasdasdasdasdas
"""

#para dizer se está em um ambiente de teste ou não
teste = True 
print('estou ? ' , teste)


# INICIAR COM LETRA, PODE CONTER NÚMEROS, SEPARAR _, LETRAS MINÚSCULAS

nome = 'erica'
idade = 20 #INT
altura = 1.64 #FLOAT
e_maior = idade > 18 #bool 
peso = 42

#outro exemplo 
data_1 = False 
data_2= True

print('Nome : ' , nome)
print('idade : ' , idade)
print('altura : ' , altura)
print('e maior de idade : ' , e_maior)

print(altura * idade)

# a divisão sera inteira com // 
imc = peso // (altura * altura)

#imc
print( nome, 'tem ' , idade ,' anos de idade e o seu imc e', imc)




#type para ve o valor da variável
print(nome, type(nome))
