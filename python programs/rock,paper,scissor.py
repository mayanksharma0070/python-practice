# A python program to play rock paper scissor

import random as rdm
options = ("rock", "paper", "scissor")
ans = 'y'

while(ans.lower() == 'y'):
    print("\nenter your choice")
    print("For ROCK press 1")
    print("For PAPER press 2")
    print("For SCISSOR press 3")
    choice = input("Your choice(1, 2 or 3): ")

    if choice not in ["1", "2", "3"]:
        print("Invalid input! (1/2/3)")
        continue

    comp = rdm.choice(options)

    # Converting user choice number to text
    if choice == "1":      player = "rock"
    elif choice == "2":    player = "paper"
    else:                  player = "scissor"

    print("\nYou choose:", player.upper())
    print("Computer chooses:", comp.upper(), "\n")

    # Game Logic
    if player == comp:
        print("Oho!! Same to same... It's a DRAW!")
    elif (player == "rock" and comp == "scissor") or \
         (player == "paper" and comp == "rock") or \
         (player == "scissor" and comp == "paper"):
        print("lucky you! You WIN 🎉")
    else:
        print("Haha Noob.! Computer WINS 😎")

    ans = input("\nWant to play again (y/n)?: ")

print("\nGame Over...\nThank you for playing Bye Bye 👋")
