'''conversão de tipos, coerção
type convertion, typecasting, coercion -> é o ato de converter um tipo em outro
tipos imutáveis e primitivos -> str, int, float, bool
'''

print('1',type('1')) #sem coerção
print(int('1'),type(int('1'))) #coerção foi feita
print(int('1') + 1) #coerção de string para int e soma
print(float('1.7') + 1) #coerção de string para float e soma
print(str(11)+'b') #coerção de int para string e concatenação