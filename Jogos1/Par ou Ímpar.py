#JOGO DE PAR OU IMPAR
print("-*"*20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("*-"*20)

from random import randint
vitorias = 0
from time import sleep

while True:
    valor = int(input('Digite um valor: ').strip())
    lado = input('Quer PAR ou ÍMPAR? [P/I] ').strip()
    computador = randint(1, 100)
    print("-" * 20)
    sleep(1)
    print(f"Eu jogo {computador}")
    soma = valor + computador
    print(f"Deu {soma}", end=" ")

    if soma % 2 == 0:
        print("e é PAR")
        print("-" * 20)
        sleep(1)
        if lado in 'Pp':
            print("Você ganhou essa!")
            vitorias += 1
        else:
            print("Você perdeu!")
            break

    elif soma % 2 != 0:
        print("e é ÍMPAR")
        print("-" * 20)
        sleep(1)
        if lado in 'Ii':
            print("Você ganhou essa!")
            vitorias += 1
        else:
            print("Você perdeu!")
            break
    print("-" * 20)
    if valor < 0:
        break
print("*-*"*20)
print(f"GAME OVER! Você ganhou {vitorias} partidas.")