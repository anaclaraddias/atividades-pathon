#exercicio 5

catetoO = float(input("Digite o valor do cateto oposto ->"))
catetoA = float(input("Digite o valor do cateto adjacente ->"))

hipotenusa = ((catetoO ** 2) + (catetoA ** 2)) ** 0.5

print(f"A hipotenusa desse triangulo e igual a: {hipotenusa:.2f}")

