notas = ("matemática",17.5,"fisica",21,"portugues",21.9)
print("-" *40)
print("{:*^40}".format("Boletim Escolar"))
print("-" *40)
for x in notas:
    if notas.index(x)%2 == 0:
        nome = x
        nota = notas[notas.index(x)+1]
        print("{:-<35}{:>5}".format(nome,nota))
              

