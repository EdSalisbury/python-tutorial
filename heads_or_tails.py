import random
import time

def coinflip():
    val = random.randint(0,1)
    
    if val:
        return "heads"
    return "tails"

guess = ""
while not guess:
    guess_input = input("Heads or tails (H/T): ")

    if guess_input.upper().strip() == "H" or guess_input.upper().strip() == "HEADS":
        guess = "heads"
    elif guess_input.upper().strip() == "T" or guess_input.upper().strip() == "TAILS":
        guess = "tails"

print(f"You chose {guess}")
print("Flipping the coin.", end="", flush=True)
time.sleep(1)
print(".", end="", flush=True)
time.sleep(1)
print(". ", end="", flush=True)
time.sleep(2)
result = coinflip()
print(f"and it's {result}!")

if result == guess:
    print("YOU WIN!")
else:
    print("YOU LOSE!")


