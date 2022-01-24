"""
Como 'retornar' mais de um objeto

° É possível retornar 2 'coisas' ? 2 listas, 2 strings, 2 números...
    ° Sim, basta retornar como uma tupla com 2 itens( vamos fazer um exemplo)
"""



def operacoes_basicas(num1, num2):
    soma = num1 + num2
    diferenca = num1 - num2
    mult = num1 * num2
    divisao = num1 / num2
    return (soma, diferenca, mult, divisao ) # mesmo sem  o parêntes ele ainda ira retornar uma tupla

print(operacoes_basicas(10,2))
