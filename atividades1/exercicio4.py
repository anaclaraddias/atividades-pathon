#exercicio 4 2.0 (agr com while)

reais = float(input("Digite o valor em reais ->"))

dolar = reais / 4.98

#perguntar se quer inteiro ou com centavos

while True:

    resposta = int(input("Voce deseja receber seu resultado em um valor inteiro (Digite 1) ou em um valor com centavos (Digite 2)?"))

    if resposta == 1:

        print(f"O valor R$ {reais} e equivalente a aproximadamente US$ {dolar:.0f}")
        break

    elif resposta == 2:

        print(f"O valor R$ {reais} e equivalente a US$ {dolar:.2f}")
        break

    else:

        print("Digite uma opcao valida")
        continue
