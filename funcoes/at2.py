def imprimesequencia(n):
    for linha in range(1, n + 1):
        for numero in range(1, linha + 1):
            print(numero,end=" ")
        print(" ")

a = int(input("Digite um número: "))
imprimesequencia(a)

a = int(input("Digite outro número: "))
imprimesequencia(a)
