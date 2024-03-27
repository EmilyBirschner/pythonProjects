'''While else'''

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    
    if letra == 'y':
        break
    
    print(letra)
    i += 1
else:
    print ('Não foi encontrado nenhum "y" na frase')
print('Fora do while.')