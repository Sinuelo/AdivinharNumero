import random


def chute(x):
    numero_aleatorio = random.randint(1,x)
    chute = 0
    numero_tentativas = 0
    while chute != numero_aleatorio:
        chute = int(input(f"Digite um número entre 1 e {x}: "))
        numero_tentativas +=1
        if chute < numero_aleatorio:
            print("Tente de novo, o número secreto é maior")
        elif chute > numero_aleatorio:
            print("Tente de novo, o número secreto é menor")

    print(f"Parabéns, você adivinhou o número secreto corretamente em {numero_tentativas} tentativa(s)")


chute(10)