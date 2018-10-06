import math
def fator(a,b):
    while True:
        print("""
             1-adição
             2-subtração
             3-divisão
             4-multiplicação
             5-sair             
             """)
        op = 0
        op = int(input("Digite uma opção: "))
        if op == 1:
            return a + b
        if op == 2:
            return a - b
        if op == 3:
            return a / b
        if op == 4:
            return a * b
        if op == 5:
            break
            
            
              
