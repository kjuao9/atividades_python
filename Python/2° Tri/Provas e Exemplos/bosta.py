op = 0
while True:
    print('''
    1 - somar
    2 - subtrair
    3 - multiplicar
    4 - sair do menu
    ''')
    op = int(input("Escolha uma opçao"))
    num1 = int(input("Primeiro Número"))
    num2 = int(input("Segundo Número"))

    if op == 4:
        print("FUI!!!")
        break

    if op == 1:
        resp = num1 + num2
        print("O resultado é",resp)

    if op == 2:
        resp = num1 - num2
        print("O resultado é",resp)

    if op == 2:
        resp = num1 * num2
        print("O resultado é",resp)
