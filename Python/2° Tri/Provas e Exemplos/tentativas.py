tentativas = 0
while True:
    nome = input("Digite seu nome")
    if nome != "joao":
        continue
    senha = input("Digite a senha")
    if senha == "123":
        print("Acesso autorizado")
        break
    tentativas = tentativas + 1
    if tentativas > 5:
        print("Excedeu o maximo de tentativas")
        break
    print("Voce ainda tem", 5 - tentativas, "tentativas")
     
    
