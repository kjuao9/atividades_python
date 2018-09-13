gph = float(input("Quanto você ganha por hora ?"))
nht = float(input("Número de horas trabalhadas por mês?"))
salbr = gph + nht
i = salbr
print("O seu salario bruto e igual a:",salbr,"R$")
c = salbr /100 //8
print("O dinheiro pago ao INSS foi:",i,"R$")
b = salbr /100 / 5
print("O dinheiro pago ao sindicato foi:",c,"R$")
a = salbr *100 - 11
sal =(a + b / c *i)
print("O seu salario liquido foi",i,"R$")

