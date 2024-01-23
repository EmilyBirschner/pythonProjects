# Introdução ao try/except
# try -> tentar executar o código
# except -> ocorreu algum erro ao executar

numero_str = input('Vou dobrar o número que você digitar: ')
try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')