#Jogo de Adivinhação
import random
from random import randint

print("Tente adivinhar o número que escolhi...")
num = random.randint(1, 999)
tentativa = int(input('Qual número você acha que é? ').strip())
print("=-="*20)

if (num == tentativa):
    print(f"Parabéns, você acertou o número, o número era {num}.")
else:
    print(f"Você errou, talvez acerte da próxima vez.")
    print(f"Meu número escolhido era {num}.")