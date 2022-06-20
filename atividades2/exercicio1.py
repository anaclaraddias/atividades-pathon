
num = int(input("Digite um numero ->"))

multiplos = []

i = 1

while i <= 10:

    res = num * i

    multiplos.append(res)

    i += 1


print(f"Multiplos de {num} --> {multiplos}")
    