n1 = float(input("Qual o primeiro número ?"))
n2 = float(input("Qual o segundo número ?"))
n3 = float(input("Qual o terceiro número ?"))
if (n1 > n2):
    print(n1)
    if(n2 > n3):
        print(n2)
        if(n3 > n1):
            print(n3)
        else:
            print(n1)
    else:
        print(n3)
else:
    print(n2)
 
