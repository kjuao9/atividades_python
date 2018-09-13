op = 0
while True:
    print('''
    1 - Somar
    2 - Subtrair
    3 - Dividir
    4 - Multiplicar
    5 - Sair
    ''')
    op = int(input("Escolha uma opçao"))

    if op == 5:
        print("Desligando...")
        break
    
    num1 = int(input("Primeiro Número"))
    num2 = int(input("Segundo Número"))

    if op == 1:
        resp = num1 + num2
        print("O resultado é",resp)

    if op == 2:
        resp = num1 - num2
        print("O resultado é",resp)

    if op == 3:
        resp = num1 / num2
        print("O resultado é",resp)

    if op == 4:
        resp = num1 * num2
        print("O resultado é",resp)
