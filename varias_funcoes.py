import math

def letras():
    palavra = input("Digite a palavra: ")
    vogais = 0
    consoantes = 0
    for x in palavra:
        if x in "aeiou":
            vogais = vogais + 1
        else:
            consoantes = consoantes + 1
    print("A palavra",palavra,"tem",len(palavra),"letras; dentre elas",vogais,"vogais e",consoantes,"consoantes.")

def calculadora(x,y):
    resp = 0
    print("""
          1-adição
          2-subtração
          3-multiplicação
          4-divisão
          5-potenciação
          6-raiz
          7-sair
          """)
    while True:
        op = int(input("Escolha uma opção: "))
        if op == 1:
            resp = x + y
            return resp
        if op == 2:
            resp = x - y
            return resp
        if op == 3:
            resp = x * y
            return resp
        if op == 4:
            resp = x / y
            return resp
        if op == 5:
            resp = x ** y
            return resp
        if op == 6:
            resp = math.pow(x, 1/y)
            return resp
        if op == 7:
            print("Desligando...")
            break
        
    
    
        
    
