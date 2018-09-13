fdia = int(input("Quantidade de cigarros fumados por dia ?"))
fpano = int(input("Por quantos anos voce fumou ?"))
fano = fdia * 365
qd = fano * fpano
qd = qd * 11
pi = qd // 60
print("Voce perdera",pi,"dias da sua vida fumando")

