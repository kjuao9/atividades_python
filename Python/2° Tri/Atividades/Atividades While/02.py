x = 0
soma = 0
while True:
    x = int(input("Digite o valor do produto"))
    soma = x
    soma = soma + soma
    if x == 0:
        break
print(soma)

