print("Palindrome program!")

array = ["rotor", "kayak", "racecar", "trees", "desk", "refer", "madam", "table", "tacocat", "white"]

for word in array:
  letter_position = 0
  letter_matches = 0
  halfway = len(word) // 2
  
  while letter_position < halfway:
    if word[letter_position] == word[len(word) - 1 - letter_position]:
      letter_matches += 1
      letter_position += 1
    else:
      print(word, "is not a palindrome")
      letter_position = halfway
    
    if letter_matches == halfway:
      print(word, "is a palindrome")
      letter_position = halfway
      
print("Goodbye!")
    
 
  
