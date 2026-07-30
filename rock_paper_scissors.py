import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"


def main():
    user_score = 0
    computer_score = 0
    choices = ["rock", "paper", "scissors"]

    print("\n=== Rock Paper Scissors ===")

    while True:
        user_input = (
            input("\nEnter Rock, Paper, Scissors (or 'quit' to exit): ")
            .strip()
            .lower()
        )

        if user_input == "quit":
            print(
                f"\nFinal Score -> You: {user_score} | Computer: {computer_score}"
            )
            print("Thanks for playing!")
            break

        if user_input not in choices:
            print("❌ Invalid choice! Choose Rock, Paper, or Scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(user_input, computer_choice)

        if result == "tie":
            print("🤝 It's a tie!")
        elif result == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1

        print(f"Current Score -> You: {user_score} | Computer: {computer_score}")


if __name__ == "__main__":
    main()