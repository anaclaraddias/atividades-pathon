#exercicio 2
# distribuidor 28%
# impostos 45%

custoF = float(input("Diigite o custo de fabrica  ->"))

porcentD = custoF * 0.28
porcentI = custoF * 0.45

custoT = custoF + porcentD + porcentI

print(f"Porcentagem de distribuidor: {porcentD:.2f}")
print(f"Porcentagem de impostos: {porcentI}")
print(f"Custo final ao consumidor: R$ {custoT}")


