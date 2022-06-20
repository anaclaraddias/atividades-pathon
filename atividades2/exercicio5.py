
while True:

    usuario = input("Digite seu usuario -> ")

    if len(usuario) >= 12 and "!" not in usuario and "@" not in usuario and "#" not in usuario:

        while True:

            senha = input("Digite sua senha -> ")

            if len(senha) >= 8:

                if "1" in senha or "2" in senha or "3" in senha:

                    print("Conta criada!")

                    break

                else:

                    continue

            else:

                continue


        break

    else:

        continue