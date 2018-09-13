
x = 0
verde = 0
vermelho = 0
branca = 0
while x < 5:
    voto = input("Escolha uma cor :verde = vd, vermelho = vm, e branca = b")
    if voto == "vd":
        verde = verde + 1
    if voto == "vm":
        vermelho = vermelho + 1
    if voto == "b":
        branca = branca + 1
    x = x + 1
print(verde,"pessoa(s) votou(aram) para verde,",vermelho,"votou(aram) para vermelho e",branca,"pessoa(s) votou(aram) para branca")
    
    
