p1 = input("Telefonou para a vítima ?")
p2 = input("Esteve no local do crime ?")
p3 = input("Mora perto da vítima ?")
p4 = input("Devia para a vítima ?")
p5 = input("Já trabalhou com a vítima ?")
resp = 0
if p1 == "sim":
    resp = resp + 1
if p2 == "sim":
    resp = resp + 1
if p3 == "sim":
    resp = resp + 1
if p4 == "sim":
    resp = resp + 1
if p5 == "sim":
    resp = resp + 1

if resp == 2:
    print("Suspeito")
elif resp == 3 or resp == 4:
    print("Cumplice")
elif resp == 5:
    print("Culpado")
else:
    print("Inocente")
