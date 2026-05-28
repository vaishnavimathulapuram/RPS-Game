import random

print("===================================")
print(" ROCK PAPER SCISSORS GAME ")
print("===================================")

print("Type:")
print("- rock")
print("- paper")
print("- scissors")
print("- bye to stop\n")

# Score variables
user_score = 0
computer_score = 0

# Choices list
choices = ["rock", "paper", "scissors"]

while True:

    # User input
    user_choice = input("You: ").lower().strip()

    # Exit game
    if user_choice == "bye":

        print("\nGame Over!")
        print("Final Scores:")
        print("You:", user_score)
        print("Computer:", computer_score)
        break

    # Invalid input
    if user_choice not in choices:

        print("Invalid choice. Try again.\n")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print("Computer:", computer_choice)

    # Match draw
    if user_choice == computer_choice:

        print("Result: Match Draw!")

    # User wins conditions
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):

        print("Result: You Win!")
        user_score += 1

    # Computer wins
    else:

        print("Result: Computer Wins!")
        computer_score += 1

    # Display scores
    print("\nScores:")
    print("You:", user_score)
    print("Computer:", computer_score)

    print("-----------------------------------")