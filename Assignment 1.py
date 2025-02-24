# Part 1: Even or Odd

print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")

a = int(input("Please enter your first number: "))
b = int(input("Please enter your second number: "))

if (a % 2 == 1 and b % 2 == 1):
  print("The product ", a, "x", b, " will be odd.")
elif (a % 2 == 0 and b % 2 == 0):
  print("The product ", a, "x", b, " will be even.")
elif (a % 2 == 1 and b % 2 == 0):
  print("The product ", a, "x", b, " will be even.")
else:
    print("The product ", a, "x", b, " will be even.")

# Part 2: The inner (or body) diagonal of a cube
import math

print("I will find the cube's inner diagonal for any edge length!")

a = int(input("Please enter the edge length of your cube:"))
d = a * math.sqrt(3)

print("The length of the inner diagonal of a cube with side length 8 is: %.2f" % d)

# Part 3: Making change in coins

change = int(input("Please enter the amount of change in cents:"))

if (change >= 100):
  change -= 100
  
  if (change >= 25):
    quarters = change/25
    change = change % 25
    
    if (change>= 10):
      dimes = change/10
      change = change % 10
      
      if (change >= 5):
        nickles = change/5
        change = change % 5
        
        if (change >=1):
          pennies = change/1
          change = change % 1
          
else:
  print(" %.0f %.0f %.0f %.0f " % quarters, dimes, nickles, pennies)
        



  





    
    print("The number of quarters used is %.0f" % quarters)
  
