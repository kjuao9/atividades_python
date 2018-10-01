n = 10
def soma(a:int,b:int,c=100) -> int:
    '''
    Soma de três números.
    '''
    global n
    n = 30
    resp = a + b + c
    return resp

def moldura(texto):
    tam_texto = len(texto)
    print("-"*(tam_texto+4))
    print("| {} |".format(texto))
    print("-"*(tam_texto+4))

moldura("IFNMG")
