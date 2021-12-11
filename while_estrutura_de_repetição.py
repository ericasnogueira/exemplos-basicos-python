"""
while 
utilizado para realizar ações ENQUANTO
uma codição for verdadeira.
"""  


"""while True: #loop infinito
    nome = int('qual o seu nome : ')
    print(f'Olá {nome}')
   """
a= 0
while a <5:
    #pulando o número 3
    if a == 3 :
        a = a +1
        continue #quando for 3 ele vai voltar e ir para o 4
    print(a)
    a =a + 1
    
print('acabou')

x =0 #coluna


while x <10:
    y =0 #linha
    while y < 5:
        print(f'{x} , {y}')
        y+=1
    x+=1       #x = x + 1 
print('acabou')

#calculadora

while True:
    print()
    num1= input('digite um número :')
    num2= input('digite outro numero :')
    operador = input('digite um operador :')
    sair = input('deseja sair ? [s]im ou [n]ão : ')
    
    #saindo da calculadora
                  #ou
    if sair == 's' or sair =='S':
        print('saindo da calculadora')
        break
    
    #se o que for digitado ão for um número
    if not num1.isnumeric() or not num2.isnumeric():
        print("Invalid (precisa ser um número e um operador valido) ")
        continue
    
    num1 = int(num1)
    num2 = int(num2)
    
    # + - / * 
    
    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else : 
        print('operador Invalid')
    
