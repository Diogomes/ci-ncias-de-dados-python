x =1
y=2
x+y
# add_numeros é uma função que pega dois números e os soma.
def add_numeros(x,y):
    return x+y
add_numeros(1,2)
'''add_numeros atualizados para 
obter um terceiro parâmetro opcional. 
O uso da impressão permite a impressão 
de várias expressões em uma única célula.'''
def add_numeros(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numeros(1,2))
print(add_numeros(1,2,3))
'''função adicionar numeros atualizados para obter 
um parâmetro de sinalizador opcional.'''
def add_numeros(x,y,z=None,flag=False):
    if(flag):
        print("Flag é verdadeira!")
    if(z==None):
        return x + y
    else:
        return x + y + z
print(add_numeros(1, 2, flag=True))

#atribuir a função à variável a.
def add_numeros(x,y):
    return x+y

a = add_numeros
a(1,2)


#Tipos e Sequências
print("Tipos e sequências em Python: ")

print(type('Isso é uma string'))#string
print(type(None))#vazio
print(type(1))#int
print(type(1.0))#float

#tipos de estruturas imutáveis (tuplas)
x = (1, 'a', 2, 'b')
type(x)

#tipos de estuturas mutáveis (lista)
x = [1, 'a', 2, 'b']
type(x)

#usar append para anexar um objeto a uma lista
x.append(3.3)
print(x)

#como percorrer cada item da lista.
for item in x:
    print(item)

#Ou usando o operador de indexação:

i=0
while( i != len(x) ):
    print(x[i])
    i = i + 1
#listas concatenadas "+"
[1,2] + [3,4]

#usar * para repetir listas

[1]*3

#usar operador in para verificar se algo está na lista
1 in [1 ,2 , 3]

#Agora vamos ver as strings. 
# Use a notação de colchete para cortar uma sequência.

x = 'é uma string'
print(x[0]) #primeiro caracter
print(x[0:1]) #primeiro caractere, mas definimos explicitamente o caractere final
print(x[0:2]) #primeiros dois caracteres

#Isso retornará o último elemento da sequência.

print(x[-1])

#Isso retornará a fatia começando do 
# 4º elemento do final e parando antes do 2º elemento do final.
print(x[-4:-2])

#Esta é uma fatia do início
#  da sequência e parada antes do terceiro elemento.
print(x[:3])

#E essa é uma fatia 
# que começa no quarto elemento da string e vai até o final.

print(x[3:])

primeironome = 'Azael'
ultimonome = 'Gomes'

print(primeironome + ' ' + ultimonome)
print(primeironome*3)
print('Azael' in primeironome)

#`split` retorna uma lista de todas as palavras em uma string
#  ou uma lista dividida em um caractere específico.

primeironome = 'Azael do Nascimento Santos Gomes'.split(' ')[0] # [0] seleciona o primeiro elemento da lista
ultimonome = 'Azael do Nascimento Santos Gomes'.split(' ')[-1] # [-1] seleciona o ultimo elemento da lista
print(primeironome)#string concatenada 
print(ultimonome)#string concatenada

#Certifique-se de converter objetos 
# em seqüências de caracteres antes de concatenar
a ={'Azael', }

print(a+2)

{'Azael'} + str(2)