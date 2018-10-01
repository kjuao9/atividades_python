def dizola():
    print("Olá Mundo!")
    
def diznome(nome):
    print("Olá {}, tudo bem?".format(nome))
diznome("João")
diznome("Paulo")

#int definirá que o valor deve ser inteiro

def soma(*lista) -> int:
    '''
    Funcao Soma: calcula a soma de dois números
    '''
    resultado = 0
    for x in lista:
        resultado += x
        
    return resultado
#ou: return sum(lista)

def subtracao(n1:int,n2:int) -> int:
    '''
    Funcao Soma: calcula a soma de dois números
    '''
    resultado = n1 - n2
    return resultado

import math

x = 10

def contexto():
    global x
    x = 20
    y = 50
    def teste():
        return "Teste"
    
    print(teste())        
    
    print(x)
