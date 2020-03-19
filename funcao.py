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

type('This is a string')
type(None)
type(1)
type(1.0)
