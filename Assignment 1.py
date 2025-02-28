# Part 1: Even or Odd

"""
   Author : Joshua Li
   Revison date : 2 Febuary 2025
   Program : Even or Odd
   Description : A program to determine if the product of 2 numbers will be even or odd
   VARIABLE DICTIONARY :
     a (int) = The first number the user inputted  
     b (int) = The second number the user inputted 
"""

print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")
# Prints out description of what the program will do

a = int(input("Please enter your first number: "))
# Asks and waits for the users input for the first number
b = int(input("Please enter your second number: "))
# Ask and waits for the unders input for the seecond number

if (a % 2 == 1 and b % 2 == 1):
  # Checks if both the first number and second number is odd
  print("The product ", a, "x", b, " will be an odd number.")
  # Prints out the result of the 2 numbers will be odd since both the first and second numbers are odd
  
elif (a % 2 == 0 and b % 2 == 0):
  # Checks if both the first number and second number is odd
  print("The product ", a, "x", b, " will be an even number.")
  # Prints out the result of the 2 numbers will be even since both the first and second numbers are even

elif (a % 2 == 1 and b % 2 == 0):
  # Checks if the first number is odd and if the second number is even
  print("The product ", a, "x", b, " will be an even number.")
  # Prints out the result of the 2 numbers will be even since one of the numbers is even and one of the numbers is odd
  
else:
  print("The product ", a, "x", b, " will be an even number.")
  # This will run when the first number is even and the second number is off

# Part 2: The inner (or body) diagonal of a cube

"""
   Author : Joshua Li
   Revison date : 2 Febuary 2025
   Program : Length of a Diagonal in a Cube
   Description : A calculator to determine the inner length or diagonal of a cube
   VARIABLE DICTIONARY :
     a (int) = The edge length of the cube that the user inputted  
     d (float) = The length of the diagonal of a cube with the edge length the user inputted  
"""

import math

print("I will find the cube's inner diagonal for any edge length!")
# Prints out description of what the program will do

a = int(input("Please enter the edge length of your cube:"))
# Asks user for a number as an edge length of the cube
d = a * math.sqrt(3)
# Calculates the diagonal of the cube (variable d) by using the number the user inputted 
d = round(d, 2)
# Rounds the value of the diagonal for the cube to 2 decimal places

print("The length of the inner diagonal of a cube with side length %.f is: %.2f" % (a,d))
# Prints out the length of the inner diagonal of the cube with the side length the user inputted

# Part 3: Making change in coins

"""
   Author : Joshua Li
   Revison date : 2 Febuary 2025
   Program : Making Change in Coins
   Description : a Program that makes change for amounts less than $1.00 using the fewest coins
   VARIABLE DICTIONARY :
     quarters (int) = The number of quarters after dividing the total change by 25 
     dimes (int) = The number of dimes after dividing the total change by 10
     nickles (int) = The number of nickles after dividing the total change by 5
     pennies (int) = The number of pennies after dividing the total change by 1
     change (int) = The amount of change the user inputted
     total_change (int) = The amount of change the user inputted without dividing by quarters, dimes, nickles, or pennies
"""

quarters = 0
dimes = 0
nickles = 0
pennies = 0
# Defines variables and makes them global scope

change = int(input("Please enter the amount of change in cents: "))
# Asks user to input an amount of change
total_change = change

if change % 100 == 0:
# Checks if the amount of change given is not a factor of 100
  print("No amount of change can be made except dollar coins.")
  # Prints out "no amount of change can be made except for dollar coins"
  quit()
  # Ends code

print(change, "cents can be ", end="")
# Prints out the number of cents the user inputted and then does not go to a new line which is what end="" does

if change >= 100:
    change = change % 100
    # If the change is greater than 100, it will divide by 100 and use the remainder as cents

if change >= 25:
# This will run when the change is greater or equal to 25 or when quarters can be divded into the remainding change
    quarters = int(change / 25)
    # This will set the number of quarters equal to the change divided by 25 but without the decimals
    change = change % 25
    # This calculates the remainder of change left after taking out as many quarters possible

if change >= 10:
# This will run when the change is greater or equal to 10 or when quarters can be divded into the remainding change
    dimes = int(change / 10)
    # This will set the number of dimes equal to the change divided by 10 but without the decimals
    change = change % 10
    # This calculates the remainder of change left after taking out as many dimes possible

if change >= 5:
# This will run when the change is greater or equal to 5 or when quarters can be divded into the remainding change
    nickles = int(change / 5)
    # This will set the number of dimes equal to the change divided by 5 but without the decimals 
    change = change % 5
    # This calculates the remainder of change left after taking out as many nickles possible

if change >= 1:
# This will run when the change is greater or equal to 1 or when quarters can be divded into the remainding change
    pennies = int(change / 1)
    # This will set the number of pennies equal to the change divided by 5 but without the decimals

if total_change == 1:
# If the amount of change is 1 penny 
  print("1 cent can be 1 penny.")
  # Prints out 1 cent will be 1 penny.

if quarters > 0:
# If you have at least 1 quarter this code will run
    if quarters > 1:
    # When quarters is greater than 1
        print(quarters, "quarters", end="")
        # Prints out the number of quarters, then the word quarters (plural) and end="" makes it so that the print statment will not go to the next line
    else:
    # When quarters is equal to 1
        print("1 quarter", end="")
        # Print out 1 quarter (no plural) and will not go to the next print line
    if dimes >= 1 or nickles >=1 or pennies >= 1:
    # Checks if there are dimes, nickles, or pennies left
      print(", ", end="")
      # Print out a comma since there are still more values to be printed after quarters
    if (dimes >= 1 and nickles == 0 and pennies == 0) or (dimes == 0 and nickles >= 1 and pennies == 0) or (dimes == 0 and nickles == 0 and pennies >= 1):
    # Checks if there is only 1 more value of dimes, nickles, or pennies in the list
      print("and ", end="")
      # Prints "and" since there is only 1 more value to be listed
    if dimes == 0 and nickles == 0 and pennies == 0:
    # Checks if there are any values left to be listed
      print(".")
      # Prints a period since there are no more values to be listed

if dimes > 0:
# If you have at least 1 dime this code will run
    if dimes > 1:
    # When dimes is greater than 1
        print(dimes, "dimes", end="")
        # Prints out the number of dimes, then the word quarters (plural) and end="" makes it so that the print statment will not go to the next line
    else:
        print("1 dime", end="")
        # Print out 1 dime (no plural) and will not go to the next print line 
    if nickles >= 1 or pennies >= 1:
    # Checks if there are nickles, or pennies left
      print(", ", end="")
      # Print out a comma since there are still more values to be printed after dimes
    if (nickles >= 1 and pennies == 0) or (nickles >= 0 and pennies == 1):
    # Checks if there is only 1 more value of nickles or pennies in the list
      print("and ", end="")
      # Prints "and" since there is only 1 more value to be listed
    if nickles == 0 and pennies == 0:
    # Checks if there are any values left to be listed
      print(".")
      # Prints a period since there are no more values to be listed

if nickles > 0:
# If you have at least 1 nickle this code will run
    if nickles > 1:
    # When nickles is greater than 1
        print(nickles, "nickles", end="")
        # Prints out the number of dimes, then the word quarters (plural) and end="" makes it so that the print statment will not go to the next line
    else:
        print("1 nickle", end="")
        # Print out 1 nickle (no plural) and will not go to the next print line 
    if pennies >= 1:
    # Checks if there are any pennies 
      print(" and ", end="")
      # It would print an "and" since there are pennies left to be listed in the final print statement
    if pennies == 0:
    # If there are no pennies and nothing else to be listed
      print(".")
      # It will print out a period thus end of the sentance

if pennies > 0:
  # Check if pennies are greater than 0
  print("and ", end="")
  if pennies > 1:
    print(pennies, "pennies.")
     # If pennies is greater than 1 thus being plural it will print pennies instead of penny
  else:
    print("1 penny.")
      # If there is only 1 penny then it would print penny since it is not plural 
