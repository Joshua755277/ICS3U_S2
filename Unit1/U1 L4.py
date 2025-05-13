# Predict
# I predict that the program will first ask for you to input a whole number and set the variable num to the number inputted
# Then it will will change the number you inputted into a integer type variable
# Then a new variable is created which is equal to the first variable divided by 6
# Finally it will print out the number you inputted but divded by 6

# Run
# My prediction is correct

# Inspect
# It stopped execution after the very first line since it was waiting for the user to input a number
# I inputted the number 12 and the output was 2 which matches my calculator when I divide 12 by 6

# Modify
num = input("Please input a whole number: ")
num = int(num)
num2 = input("Please input another whole number except 0: ")
num2 = int(num2)
num3 = num/num2
print("When", num, "is divided by", num2, "the result is:", num3)

# Making sure the divisor is not 0 is important since a number being divided by 0 is not possible and thus python will crash


