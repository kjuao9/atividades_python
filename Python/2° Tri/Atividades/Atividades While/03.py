maior = -999999
menor = 999999

while True:
    n = int(input("Digite um número :"))
    if n == 0:
        break
    elif n > maior:
        maior = n
    if n < menor:
        menor = n
print("O maior número é",maior,"E o menor número é",menor)
        
