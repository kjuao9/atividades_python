tam = float(input("Qual o tamanho do arquivo em MB ?"))
vel = float(input("Qual a velocidade da velocidade em Mbps ?"))
# Conversão de MB para Mb #
tam = tam * 8 
tmp = tam // vel
m = tmp // 60
s = tmp % 60
print("O download vai demorar",m,"minutos e",s,"segundos")
