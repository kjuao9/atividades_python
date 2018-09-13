valor = int(input("Valor que deseja sacar"))
nota2 = 0
nota5 = 0
nota10 = 0
nota20 = 0
nota50 = 0
nota100 = 0
if valor < 10 or valor > 800:
    print("Não pode sacar esse valor")
else:
    notas100 = valor // 100
    valor = valor - nota100 * 100
    nota50 = valor // 50
    valor = valor - nota50 * 50
    nota20 = valor // 20
    valor = valor - nota20 * 20
    nota10 = valor // 10
    valor = valor - nota10 * 10
    nota5 = valor // 5
    valor = valor - nota5 * 5
    nota2 = valor // 2
    valor = valor - nota2 * 2

    if valor != 0:
        print("Sugiro o saque de:",nota2*2 + nota5*5 + nota10*10 + nota20*20 + nota50*50 + nota100*100,"R$")

    if nota2 != 0:
        print("Notas de R$ 2,00: ",nota2)
    if nota5 != 0:
        print("Notas de R$ 5,00: ",nota5)
    if nota10 != 0:
        print("Notas de R$ 10,00: ",nota10)
    if nota20 != 0:
        print("Notas de R$ 20,00: ",nota20)
    if nota50 != 0:
        print("Notas de R$ 50,00: ",nota50)
    if nota100 != 0:
        print("Notas de R$ 100,00: ",nota100)

