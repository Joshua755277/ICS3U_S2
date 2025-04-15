"""
   Author : Joshua Li
   Student Number : 75577
   Revison Date : 09 April 2025
   Course Code : ICS3U
   Program : Is it a Palindrome?
   Description : A program to determine which words inside an array are a palindrome or not
   VARIABLE DICTIONARY :
     word_list (collection) = An array with 10 different words with some being a palindrome
     word (string) = Singular word in the array word_list
     letter_position (int) = The position of the character in the word 
     letter_matches (int) = The number of matches between the letter and the corresponding letters from the end
     halfway (int) = The halfway point of each word 
"""

print("Palindrome program!")
# Prints instructions

word_list = ["rotor", "kayak", "racecar", "trees", "desk", "refer", "madam", "table", "tacocat", "white"]
# Creates array with 10 words

for word in word_list:
# Cycles through each word in the array
  letter_position = 0
  letter_matches = 0
  # Creates variables and sets them to 0
  halfway = len(word) // 2
  # Takes the word lengh and divdes by 2 leaving no decimal
  
  while letter_position < halfway:
  # Runs this loop when the letter position has not reached the middle of the word
  
    if word[letter_position] == word[len(word) - 1 - letter_position]:
    # Checks if the first letter in the word is equal to the last letter in the word
      letter_matches += 1
      # Increases the letter_matches by one since the first and last letter matches
      letter_position += 1
      # Increases letter_position by one in order to get to the second letter and second last letter
    else:
    # Runs if the front letter and the corresponding last letter matches
      print(word, "is not a palindrome")
      # Prints out the word is not a palindrome
      letter_position = halfway
      # Sets the letter_postion equal to the halfway number which would end the loop
    
    if letter_matches == halfway:
    # When the number of letter matches is equal to the halfway point
      print(word, "is a palindrome")
      # Prints out the word is a palindrome
           
print("Goodbye!")
# Prints Goodbye!
