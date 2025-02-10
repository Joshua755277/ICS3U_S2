# Predict
# a) If you inputted the number 6 for x and 3 for y, it would output "Now deciding if 3 is a factor of 6 ... Yes! 3 is a factor of 6"
# b) If you inputted the number 6 for x and 5 for y, it would output "Now deciding if 5 is a factor of 6 ..."

# Run
# My prediction was correct

# Inspect
# Yes it did match the output of my calculator when I tried dividing x by y

# Modify 1 and 2

import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number: ")
y = int(y)
if (y != 0):
  
  print("Now deciding if", y, "is a factor of", x, "...")
  rem = x % y
  
  if rem == 0:
      print("Yes!", y, "is a factor of", x)
  else:
      print("No!", y, "is not a factor of", x)
  
else:
  print("Please do not enter 0")
  print("A factor could not be determined")

#Modify 3
import math

x = int(input("Please enter a number between 1 and 20: "))
if ( 1 <= x <= 20):
    y = int(input("Please enter a number between 1 and 20 again: "))
    if ( 1 <= y <= 20):
        print("Now deciding if", y, "is a factor of", x, "...")
        rem = x % y
        if rem == 0:
          print("Yes!", y, "is a factor of", x)
        else:
          print(y, "is not a factor of", x)
        
    else: print(y, "is out of range. Cannot continue")
else: 
  print(x, "is out of range. Cannot continue")
  
  

  

