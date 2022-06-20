#exercicio 3

eleiT = int(input("Digite o numero total de eleitores ->"))
branco = int(input("Digite o numero de votos brancos ->"))
nulo = int(input("Digite o numero de votos nulos ->"))
validos = int(input("Digite o numero de votos validos ->"))

porcentB = (branco / eleiT) * 100
porcentN = (nulo / eleiT) * 100
porcentV = (validos / eleiT) * 100

print(f"O numero total de eleitores e: {eleiT}")
print(f"A porcentagem de votos em branco e: {porcentB} %")
print(f"A porcentagem de votos nulos e: {porcentN} %")
print(f"A porcentagem de votos validos e: {porcentV} %")








