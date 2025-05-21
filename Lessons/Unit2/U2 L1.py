# Predict
# I predict that the output when you input C, would be "I prefer cherries"
# If you were to input any other letter or symbol that is not "A", "B", or "C", it will still output "I prefer cherries" since you did not input "A" or "B" therefore it would run the else statment.

# Modify 1

print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
elif:
    print("I prefer cherries")
else:
  print("Error")

# Modify 2:

number = int(input("Enter a number from 1-100: "))

if (number >= 80) and (number <= 100):
  print("A")
elif (number >= 70) and (number <= 79):
  print("B")
elif (number >= 60) and (number <= 69):
  print("C")
elif (number >= 50) and (number <= 59):
  print("D")
elif (number >= 1) and (number <= 50):
  print("F") 
else:
  print("Invalid number")
