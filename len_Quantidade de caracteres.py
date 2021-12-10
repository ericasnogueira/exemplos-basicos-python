#quantidade de caracteres 

#checando a quantidade de caracteres com len
# não funciona com número
#aqui vai conta tambem com o espaço

#exemplo 1 
usuario = input("Digite seu Usuario : ")
qtd_caracteres =  len(usuario)


#primeira checagem
print(usuario,qtd_caracteres, type(qtd_caracteres))

#checando se tem 6 caracteres

if qtd_caracteres < 6:
    print('Voce precisa digitar pelo menos 6 caracteres ')
else: 
    print('foi cadastrado com sucesso')
    
    
#exemplo 2 

#pegando duas str e somando a quantidade de caracteres

string1 = input('Digite alguma coisa : ')
string2 = input('Digite outra coisa : ')
                                                                #somando as duas str
print(f' a quantidade total digitada de caracteres digitados foi {len(string1) + len(string2)}')
    
