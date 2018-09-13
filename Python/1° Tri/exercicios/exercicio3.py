#Exercício 3#
peso = int(input("Qual é o peso de peixes em kg pescados ?"))
if peso > 50 :
 exc = peso - 50
 print("Há excesso de peixes em",exc,"kg")
 mul = exc * 4
 if peso > 50:
      print("Você deverá pagar uma multa de",mul,"R$")
 else:
      print("Não há multa")
else:
  print("Não há nenhum excesso de peixes")
