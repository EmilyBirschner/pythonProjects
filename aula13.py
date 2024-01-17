#Introdução a formatação de Strings - f-strings

nome = 'Fulano de tal'
altura = 1.80
peso = 95
imc = peso / (altura ** 2)

print(...) #Ellipsis não gera erro no código

#print(nome, 'tem', altura, 'de altura, pesa', peso, 'kg e seu IMC é:', imc)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso}kg e seu IMC é: {imc:.2f}'
print(linha_1)
print(linha_2)