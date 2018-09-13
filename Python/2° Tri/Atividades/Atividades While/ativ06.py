n = 0
maioraltura = 0
maioralturanome = 0
qtmulheres = 0
somalturamulheres = 0
medialturamulheres = 0
while n < 10:
    nome = input("nome:")
    sexo = input("sexo:")
    if sexo != "masculino" or sexo != "feminino":
        sexo = input("Digite para sexo masculino ou feminino:")
    altura = float(input("altura:"))
    if altura > maioraltura:
        maioraltura = altura
        maioralturanome = nome
    n = n + 1
    if sexo == "feminino":
        qtmulheres = qtmulheres + 1
        somalturamulheres = somalturamulheres + soma
        
print("{} tem {} e é a maior altura ".format(maioralturanome.maioraltura))
medialturamulheres = somalturamulheres / qtmulheres
print("A média de altura das mulheres é {}".format(medialturamulheres))
print("A q")
