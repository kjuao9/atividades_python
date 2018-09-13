lista = list()
while True:
    numero = int(input("Digite um valor:"))
    if numero in lista:
        continue
    else:
        lista.append(numero)
    resp = print("Deseja continuar ? (s/n)")
    if resp == "n":
        break
print(sorted(lista))
    
