import random

opcoes = ['papel', 'pedra', 'tesoura']

escolha_computador = random.choice(opcoes)
user = input("Escolha entre: papel, pedra, tesoura \n")

if user == "papel" or user == 'pedra' or user == 'tesoura':
  if user == "papel" and escolha_computador == "tesoura":
    print( "Voce perdeu")
  elif user == 'pedra' and escolha_computador == "papel":
    print("Voce perdeu")
  elif user == "tesoura" and escolha_computador == "pedra":
    print("Voce perdeu")
  else:
    print("ganhou")
print("o cpu escolheu:", escolha_computador)