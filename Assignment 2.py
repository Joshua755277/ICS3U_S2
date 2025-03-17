"""
   Author : Joshua Li
   Student Number : 75577
   Revison Date : 16 March 2025
   Course Code : ICS3U
   Program : A number guessing game
   Description : A game for the user to guess the randomly generated number using hints 
   such as if their guess is higher or lower than the desired number with only 6 attempts
   VARIABLE DICTIONARY :
     tries (int) = Counter to track the number of guesses made by the user
     answer (int) =  Randomly generated number between 1 to 100
     guess (int) =  The user's inputted guess during the game
"""
import random
# Imports random module to generate a random number
print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is.")
print("You have a maximum of six (6) tries.")
# Prints out instructions to the number guessing game

tries = 0
# Defines tries and sets it to 0
answer = random.randint(1, 100)
# Generates a random number under from 1 to 100 under the variable answer
guess_num = 1
# Counts the number of guesses

while tries < 6:
   # Runs the loop 6 times since you are only allowed 6 guesses
   tries += 1
  # Increases tries by 1 so the loop runs 6 times
  guess = int(input("Guess #%d: " % tries))
   # Asks the user for their guess

  if guess == answer:
     # Checks if the users guess is the same as the generated  number
    print("You guessed right!")
     # Prints "You guessed right!" 
    tries = 6
    # Sets tries equal to 6 thus ending the loop

  elif guess > answer:
    # Checks if the user's guess is greater than the generated answer
    print("Lower!")
    # Tells the user to guess lower

  elif guess < answer:
    # Checks if the user's guess is smaller than the generated answer
    print("Higher!")
    # Tells the user to guess higher

if guess != answer:
  # Checks if your guess is not the correct answer
  print("Sorry: you are out of guesses! The answer was %d. Better luck next time!" % answer)
  # Prints out that you did not guess the correct answer and also shows the correct answer
  
