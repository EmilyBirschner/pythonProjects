#Formatação de strings com o método format

a = 'AAAA'
b = 'BBBB'
c = 1.1

#string = 'a={} b={} c={.2f}' -> assim depende da ordem dos argumentos
#string = 'a={0} b={1} c={2:.2f}' -> com o valor dos indices, não precisa de ordem


string = ' b={nome2} a={nome1}  c={nome3:.2f}' #usando parâmentros nomeados
formato = string.format(
    nome1 = a, 
    nome2 = b, 
    nome3 = c
    )

print(formato)