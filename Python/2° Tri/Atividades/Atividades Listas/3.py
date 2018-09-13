lista = list()

for x in range(5):

    numero = int(input("Digite um número:"))

    if len(lista) == 0 or lista(-1) < numero:
        lista.append(numero)
        continue
    
    pos = 0
    while numero > lista(pos):
        pos += 1

    lista.insert(pos,numero)

print(lista)
        
        
        
    
        
