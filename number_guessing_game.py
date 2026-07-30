import json
import random


def load_highscore():
    try:
        with open("highscore.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def save_highscore(score):
    with open("highscore.json", "w") as f:
        json.dump(score, f)


def play_game():
    number_to_guess = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    high_score = load_highscore()

    print("\n=== Number Guessing Game ===")
    if high_score:
        print(f"🏆 Current Best Record: {high_score} attempt(s)")
    else:
        print("🏆 No high score yet. Set the first record!")

    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while True:
        attempts += 1
        try:
            guess = int(
                input(f"Attempt {attempts}/{max_attempts} - Enter guess: ")
            )
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            attempts -= 1
            continue

        if guess == number_to_guess:
            print(f"\n🎉 Correct! You guessed the number in {attempts} attempt(s)!")
            if high_score is None or attempts < high_score:
                print("🌟 NEW HIGH SCORE RECORD SAVED!")
                save_highscore(attempts)
            break

        if attempts >= max_attempts:
            print(
                f"\n💥 Game Over! You ran out of attempts. The number was {number_to_guess}."
            )
            break

        if guess < number_to_guess:
            print("Too low! Try higher.")
        else:
            print("Too high! Try lower.")


if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break