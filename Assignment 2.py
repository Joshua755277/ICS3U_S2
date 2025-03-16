import random
print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is.")
print("You have a maximum of six (6) tries.")

tries = 0
answer = random.randint(1, 100)
guess_num = 1

while tries < 6:
  guess = int(input("Guess #%d: " % guess_num))

  if guess == answer:
    print("You guessed right!")
    quit()

  elif guess > answer:
    print("Lower!")

  elif guess < answer:
    print("Higher!")
    
  tries += 1
  guess_num += 1

print("Sorry: you are out of guesses! The answer was %d. Better luck next time!" % answer)
