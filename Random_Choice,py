import random
import string

Options = []

print("--- RANDOM DECISION MAKER ---")
print("'Quit' to choose random & Quit")

while True:
    Add = input("What do u wanna add? ")
    
    
    if Add.strip().lower() == "quit":
        
        if Options:
            print("\nRandom choice:", random.choice(Options))
        else:
            print("No options were added!")
        break
    else:
        Text = string.capwords(Add)
        Options.append(Text)
        print(Options)

        
