n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
n3 = int(input("Digite outro número:"))
n4 = int(input("Digite só mais um número:"))
tupla = (n1,n2,n3,n4)
if 9 in tupla:
    print(' o 9 apareceu {} vez(es)'.format(tupla.count(9)))
else:
    print('o 9 não foi digitado')
if 3 in tupla:
    print(' o 3 apareceu {} vez(es)'.format(tupla.count(3)))
else:
    print('o 3 não foi digitado')
for n in tupla:
    if n%2 == 0:
        print('{} é um número par'.format(n))
