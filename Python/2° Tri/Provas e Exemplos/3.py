x = 0
maior = 0
menor = 0
while True:
    x = int(input("Digite o valor do produto"))
    n = x
    if x == 0:
        break
    if x > n:
        x = maior
        n = menor
        if n > x:
            n = maior
            x = menor
print(x,n)
            
            
    
        
