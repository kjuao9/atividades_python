todos_numeros = list()

while True:
    numero = int(input("Digite um número: "))
    todos_numeros.append(numero)
    res = input("Deseja Sair? s/n")
    if res == "s":
        break
numeros_pares = list()
numeros_impares = list()

for x in todos_numeros:
    if x % 2 == 0:
        numeros_pares.append(x)
    else:
        numeros_impares.append(x)
    
print("A lista é",todos_numeros)
print("Os números pares são",numeros_pares)
print("Os números impares são",numeros_impares)


