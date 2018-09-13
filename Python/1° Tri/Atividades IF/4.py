cartao = input("Você tem cartão ?")
tipo = input("Qual o tipo de carne comprada ?")
quantidade = float(input("Qual a quantidade de carne comprada ?"))
desconto = 0
pagamento = 0
vpaga = 0
if tipo == "contra file" or "Contra file" or "Contra File" or "Contra Filé" or "contra filé" and quantidade <= 5:
 preçot = quantidade * 35
if cartao == "sim" or "tenho" or "Sim" or "Tenho":
            desconto = 5
            pagamento = "Cartão"
            vpaga = preçot * 0.05
            
elif cartao == "nao" or "não" or "Nao" or "Não":
          desconto = 0
          pagamento = "Dinheiro"
          vpaga = preçot 
print("________________________________________________________________________________")
print("Tipo de carne: Contra Filé")
print("Quantidade: ",quantidade,"kg")
print("Preço total: ",preçot,"R$")
print("Tipo de pagamento: ",pagamento)
print("Valor do desconto: ",desconto,"%")
print("Valor a pagar: ",vpaga,"R$")
   
  
