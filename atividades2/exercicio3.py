
import random as func

velocidade = input("Digite a velocidade ->")

if velocidade == "":

    print("velocidade nao informada!")

    velocidade = func.randint(1,120) 

    print(f"Velocidade - {velocidade}") #escrevendo a nova velocidade

    if velocidade < 30:

        print("O carro esta muito lento, mude de mao")

    elif velocidade > 90:
    
        excesso = velocidade - 90

        multa = excesso * 7

        print(f"Carro acima da velocidade maxima, multa de R$ {multa}")

    else: #se a velocidade estiver entre 30 e 90, essa mensagem é escrita 
 
        print("Velocidade aceitavel")

else:

    velocidade = float(velocidade)

    if velocidade < 30:

        print("O carro esta muito lento, mude de mao")

    elif velocidade > 90:
    
        excesso = velocidade - 90

        multa = excesso * 7

        print(f"Carro acima da velocidade maxima, multa de R$ {multa}")
    
    else:
 
        print("Velocidade aceitavel") 
        