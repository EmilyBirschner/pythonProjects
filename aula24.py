# Operadores in e not in
# strings são iteráveis

#nome = 'Otávio'
#print(nome[2])
#print(nome[-4])
#print ('á' in nome)
#print ('z' in nome)
#print(10 * '-')
#print ('á' not in nome)
#print ('z' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')