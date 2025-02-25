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

change = int(input("Please enter the amount of change in cents:"))

# Part 3: Making change in coins

if (change >= 100):
  change -= 100
  
  if (change >= 25):
    quarters = change/25
    print("%.0f cents can be %.0f quarters." % (change, quarters))
    change = change % 25
    
    if (change>= 10):
      dimes = change/10
      print("%.0f cents can be %.0f quarters, and %0.f dimes." % (change, quarters, dimes))
      change = change % 10
      
      if (change >= 5):
        nickles = change/5
        print("%.0f cents can be %.0f quarters, %0.f dimes, and %0.f nickles." % (change, quarters, dimes, nickles))
        change = change % 5
        
        if (change >=1):
          pennies = change/1
          print("%.0f cents can be %.0f quarters, %0.f dimes, %0.f nickles, and %0.f pennies." % (change, quarters, dimes, nickles, pennies))
          change = change % 1
          
else:
  if (change >= 25):
    quarters = change/25
    print("%.0f cents can be %.0f quarters." % (change, quarters))
    change = change % 25
    
    if (change>= 10):
      dimes = change/10
      print("%.0f cents can be %.0f quarters, and %0.f dimes." % (change, quarters, dimes))
      change = change % 10
      
      if (change >= 5):
        nickles = change/5
        print("%.0f cents can be %.0f quarters, %0.f dimes, and %0.f nickles." % (change, quarters, dimes, nickles))
        change = change % 5
        
        if (change >=1):
          pennies = change/1
          print("%.0f cents can be %.0f quarters, %0.f dimes, %0.f nickles, and %0.f pennies." % (change, quarters, dimes, nickles, pennies))
          change = change % 1








change = int(input("Please enter the amount of change in cents:"))

if (change >= 100):
  change = change % 100
  
  if (change >= 25):
    quarters = change/25
    
    if (change % 10 >= 10):
      dimes = change/10
      
      if (change % 5 >= 5):
        nickles = change/5
        
        if (change % 1 >= 1):
          pennies = change/1
    
    
  else:
    print("%.0f cents can be %.0f quarters." % (change, quarters))
    
   else:
     print("%.0f cents can be %.0f quarters, and %0.f dimes." % (change, quarters, dimes))
     
     else:
       print("%.0f cents can be %.0f quarters, %0.f dimes, and %0.f nickles." % (change, quarters, dimes, nickles))
       
       else:
         print("%.0f cents can be %.0f quarters, %0.f dimes, %0.f nickles, and %0.f pennies." % (change, quarters, dimes, nickles, pennies))
     
   
   
   
   
else:
print("The amount of change is under 100")
  
        



  





    
    
  
