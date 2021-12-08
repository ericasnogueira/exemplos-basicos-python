# Introdução à formatação de string 

nome = 'erica'
idade = 20
altura = 1.64
peso = 42

imc = peso / (altura ** 2 )

#pode usar por  esses  meios 
print(nome, ' tem', idade, 'anos de idade e seu imc e', imc)

#exibindo valores formatados
print(f'{nome} tem {idade} anos de idade e seu imc e {imc}')

#exibindo no imc duas casas decimais 
print(f'{nome} tem {idade} anos de idade e seu imc e {imc:.2f}')

print('{} tem {} anos de idade e seu imc e {:.2f}'.format(nome, idade, imc))

print('{n} tem {i} anos de idade e seu imc e {im}'.format(n=nome, i=idade, im= imc))

