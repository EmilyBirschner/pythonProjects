#while e break - Estrutura de repetição
#Executa uma ação enquanto uma condição for verdadeira

condicao = True

while condicao:
    nome = input('Digite seu nome:')
    print(f'Seu nome é {nome}')
    #break
    if nome == 'sair':
        break
    
print('Acabou!')