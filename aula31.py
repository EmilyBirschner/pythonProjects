# id - A identidade do valor que está na memória
''' 
Flag - Marcar um local
None - não valor
is e is not - tipo, valor, identidade
id - Identidade
'''

#v1 = 'a'
#print(id(v1))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')
    
if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')