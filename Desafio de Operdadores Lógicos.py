#Desafio de Operadores Lógicos 

# - confirmando os 2: tv 50' + sorvete
# - confirmando apenas 1 : tv 32' + sorvete
# - nenhum confirmado : fica em casa
 
trabalho_terca = True
trabalho_quinta = True
 
 
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
saudavel = not sorvete 

print('TV 50 = {} TV 32={} SORVETE ={} SAUDAVEL={}'.format(tv_50,
tv_32,sorvete,saudavel))

