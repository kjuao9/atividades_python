from classe import cachorro


c1 = cachorro("lola", "branco", "m")
c1.latir
c2 = cachorro("rebeca", "bege", "g")
c2.morder
c3 = cachorro("nina", "laranja", "p")
c4 = cachorro("Totó", "marrom")
c5 = cachorro("Bob", "preto")

class pizza():
    def __init__(self):
        self.ingredientes = list()
        self.pedacos = 8
        
    def assar(self):
        print("Aguarde 10 minutos para ficar pronta sua pizza")

    def addIngredientes(self, i):
        self.ingredientes.append(i)
        print(i + "foi adicionado a pizza")

class pizzaborda(pizza):
    def __init__(self, saborborda):
        super.__init__(self)
        self.borda = saborborda

    def mudarborda(self, b):
        self.borda = b
        print("O sabor da borda foi alterado")
