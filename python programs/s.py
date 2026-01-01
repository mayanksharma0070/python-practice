import random as rdm

options = ("rock", "paper", "scissor")
ans = "y"

while ans.lower() == "y":
    print("Enter your choice")
    print("1. ROCK")
    print("2. PAPER")
    print("3. SCISSOR")
    choice = input("Your choice(1, 2 or 3): ")

    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Please enter 1, 2, or 3.")
        continue

    player = options[int(choice) - 1]
    computer = rdm.choice(options)

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    # Game result logic
    if player == computer:
        print("It's a DRAW!")
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
        print("You WIN! 🎉")
    else:
        print("Computer WINS! 😎")

    ans = input("Want to play again (y/n)? : ")

print("Thanks for playing! 😊")
