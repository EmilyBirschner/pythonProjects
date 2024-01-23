# Formatação de Strings com f-strings
''' 
s - string
d e i - int
f - float
.<numero de digitos>f
x e X - Hexadecimal
> - Esquerda
< - Direita
^ - Centro
= - Força o numero a aparecer antes dos zeros
sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'.{variavel: >10}')
print(f'{variavel: <10}.')
print(f'.{variavel: ^10}.')
print(f'{1000.20934029374092:.1f}')
print(f'{1000.20934029374092:,.1f}')
print(f'{1000.20934029374092:+,.1f}') #coloca o sinal de + ou - para aparecer
print(f'{1000.20934029374092:0=+10,.1f}') 
print(f'O hexadecimal de 1500 é {1500:08x}')

