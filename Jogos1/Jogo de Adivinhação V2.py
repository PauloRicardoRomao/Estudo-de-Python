#melhoria do jogo de adivinhação do ex 028

import random

print("Tente adivinhar o número que eu escolhi...")
print("-=-"*10)

n = random.randint(1, 999)
while n != random.randint(1, 999):
    #print(n)
    tentativa = int(input('Digite um número: ').strip())
    if tentativa == n:
        print("-=-"*10)
        print("VOCÊ ACERTOU!!!")
        break
    else:
        print("Você errou, tente de novo.")
        n = random.randint(1, 999)
print("-=-"*10)
print("FIM DE JOGO, VOCÊ GANHOU.")
print("-=-"*10)