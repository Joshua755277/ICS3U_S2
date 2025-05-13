# Predict 
# I predict the program will print "Please input a length: " and then waits for the user to enter a length
# It will then set the number you inputted as a float type variable and then take that number to the power of 2 and set the value to a new variable called area
# Then it will output "The area of a square of side length (length the user entered) is: (result of entered number to the power of 2)"

# Run
# My prediction was correct

# Inspect 
# The program stopped execution after the first print statement since it will wait for the user to input a number 
# I inputted the number 10 and it outputted 100.0 which matches with my calculator 

# Modify 

import math
radius = input("Please input the circles radius: ")
radius = float(radius)
area = 0.5*math.pi*math.pow(radius, 2) + 4*math.pow(radius, 2)
print("The area is:", area)

# The reason r has to be multiplied by 2 is because radius is only half the length of the square thus multiplying by 2 would be the full length of the side
