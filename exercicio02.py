''' 
Faça um programa que peça ao usuário para digitar um número inteiro, informe se esse número é par ou impar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro
'''

variavel_string = input ('digite um numero inteiro: ')

if variavel_string.isdigit():
    variavel_int = int(variavel_string)
    numero_e_par = (variavel_int % 2) == 0
    if numero_e_par:
        print('O numero digitado é par')
    else:
        print('O numero digitado é impar')
else:
    print('Você não digitou um numero inteiro')


''' 
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. EX: Bom dia 0-11, Boa tarde 12-17 e boa noite 18-23
'''

hora = input('Informe a hora: ')

if hora.isdigit():
    hora_int = int(hora)
    hora_bom_dia = hora_int >= 0 and hora_int <= 11 
    hora_boa_tarde = hora_int >= 12 and hora_int <=17
    hora_boa_noite = hora_int >=18 and hora_int <=23
    if hora_bom_dia:
        print('Bom dia!')
    elif hora_boa_tarde:
        print('Boa tarde!')
    elif hora_boa_noite:
        print('Boa noite')
    else:
        ('Não conheço essa hora')
else:
    print('Hora inválida!')


''' 
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva: "Seu nome é curto", se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que
6 escreva "Seu nome é muito grande"
'''
nome = input('digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1: 
    if tamanho_nome <= 4:
        print('seu nome é curto')
    elif tamanho_nome >=5 and tamanho_nome <=6: 
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')


