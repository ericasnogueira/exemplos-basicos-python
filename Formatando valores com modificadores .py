"""
-Formatando valores com modificadores 

:s -Texto  (strings)
:d -Inteiros (int)
:f -Números de pontos flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:.(CARACTERE) (> ou < ou ^ )(QUANTIDADE) (TIPO -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
nome ='Erica Nogueira'
num1 = 950
num2=3
num3=10
div= num3 / num2
              #uma casa decimal 
print (f'{div:.1f}')

#10 na esquerda
print(f'{num1:0>10}')
#botando o 10 para direita
print(f'{num1:0<10}')
#botando o 10 no centro
print(f'{num1:0^10}')

#formando um número inteiro para float 
print(f'{num1:.2f}')

#adicionando caracteres ao nome 
print(f'{nome:@^50}')
print(f'{nome:@<50}')

print(nome.lower()) #tudo minusculo
print(nome.upper()) #tudo maiusculo
print(nome.title()) #Primeiras letras maiusculas

