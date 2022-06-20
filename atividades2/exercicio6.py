
num = int(input("Digite um numero -> "))
pares = []

for i in range(0,num):

    if i % 2 == 0:

        pares.append(i)

print(f"\nnumeros pares entre 0 e {num}")
print(pares)

