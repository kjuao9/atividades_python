class cachorro():

    def __init__(self, n, p, t):
        
       self.nome = n
       self.pelo = p
       self.tamanho = t
              
    def latir(self):
        if self.tamanho == "m":
            print("au! au! au!")
        elif self.tamanho == "g":
            print("huff! huff! huff!")
        else:
            print("cain! cain! cain!")
                
    def morder(self):
        print(self.nome + " acabou de morder!")

