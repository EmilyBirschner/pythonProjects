#Exercício de programação com if e comparação

primeiro_valor = input('digite um valor: ')
segundo_valor = input('digite outro valor: ')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor > int_segundo_valor:
    print(f'{primeiro_valor=} é maior que o {segundo_valor=}')
elif int_primeiro_valor == int_segundo_valor:
    print(f'{primeiro_valor=} é igual ao {segundo_valor=}')
else:
    print(f'{primeiro_valor=} é menor que o {segundo_valor=}')