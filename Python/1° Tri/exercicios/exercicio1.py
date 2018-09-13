#Exercício 1#
l1 = int(input("Digite o valor do primeiro lado do triângulo:"))
l2 = int(input("Digite o valor do segundo lado do triângulo:"))
l3 = int(input("Digite o valor do terceiro lado do triângulo:"))
if (l2 - l3)< l1 <l2 +l3 and (l1 - l3) <l2 <l1 +l3 and (l1 -l2) <l3 < l1 +l2 and (l1 == l2 == l3):
 print("É um triângulo equilátero")
else:
    print("Não é um triângulo equilátero")
    if (l2 - l3)< l1 <l2 +l3 and (l1 - l3) <l2 <l1 +l3 and (l1 -l2) <l3 < l1 +l2 and (l1 != l2 !=l3 != l1):
      print("É um triângulo escaleno")  
    else:
        print("Não é um triângulo escaleno")
        if (l2 - l3)< l1 <l2 +l3 and (l1 - l3) <l2 <l1 +l3 and (l1 -l2) <l3 < l1 +l2 and (l1 == l2) or (l2 == l3) or (l3 == l1):
            print("É um triângulo isósceles")
        else:
            print("Não é um triângulo isósceles")
