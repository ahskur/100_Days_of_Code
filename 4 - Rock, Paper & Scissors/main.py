player_input = input("Bem-vindo ao campeonato de Pedra, Papel e Tesoura!\nO que você quer? Digite 0 para Pedra, 1 para Papel e 2 para Tesoura!\n")
number = int(player_input)
import random

if number == 0:
    print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''')
    computer = random.randint(0, 2)
    print(f"Computador escolheu: {computer}")
    if computer < 1:
        print("Você perdeu!")
    elif computer == 2:
        print("Você ganhou!")
    else: print("Empate!")
if number == 1:
    print('''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''')
    computer = random.randint(0, 2)
    print(f"Computador escolheu: {computer}")
    if computer < 2:
        print("Você perdeu!")
    elif computer == 0:
        print("Você ganhou!")
    else:
        print("Empate!")
if number == 2:
    print( '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')
    computer = random.randint(0, 2)
    print(f"Computador escolheu: {computer}")
    if computer < 0:
        print("Você perdeu!")
    elif computer == 1:
        print("Você ganhou!")
    else:
        print("Empate!")