
num = []
i = 0

while i < 6:

    num.append(int(input(f"{i} - Digite um numero --> ")))

    i += 1

print(f"\n {num}")

print("\n Os numeros pares sao:")

for x in num:

    if x % 2 == 0:

        print(f"- {x}")