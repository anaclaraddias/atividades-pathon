#exercicio 1 

anos = int(input("Digite sua idade em anos ->"))
meses = int(input("Em quantos meses ->"))
dias = int(input("E quantos dias ->"))

quant_a = anos * 365
quant_m = meses * 30

total = dias + quant_a + quant_m

print(f"A sua idade total em dias e igual a: {total} dias")