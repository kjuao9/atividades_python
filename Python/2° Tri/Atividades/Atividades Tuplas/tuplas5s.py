notas = ("Matemática",17.5,"Física",21,"Português",22.9,"História",25,"Geografia",24.2,"Química",29,"Biologia",20.3,"Inglês",22.3,"Espanhol",24.9,"Filosofia",18,"Sociologia",26,"Educação Física",19.2)
print("-" *40)
print("{: ^40}".format("Boletim Escolar"))
print("-" *40)
for x in notas:
    if notas.index(x)%2 == 0:
        nome = x
        nota = notas[notas.index(x)+1]
        print("{:.<35}{:>5}".format(nome,nota))
              

