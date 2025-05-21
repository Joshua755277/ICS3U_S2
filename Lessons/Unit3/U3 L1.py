# Prediction A
# The program will print out "Python"

# Prediction B
# The program will print out the first letter of the word under the variable progname

# Prediction C
# C goes thru each letter of the variable progname and goes to the next line each run

# Prediction D
# The sep makes it so that there is nothing being seperated between each letter and end makes it so it does not go down to the next line each print statment

# Prediction E
# Prints an empty line so the next print statments would not be on the same line as "Python"

# Prediction F
# C increases by 1 each time until it reaches the number of letters in progname
# Also prints out the letters of progname 1 one by one
""" 
0 P
1 y
2 t
3 h
4 o
5 n
"""

# Modify

progname = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in."
spaces = 0
for c in progname:
  if c == " ":
    spaces +=  1
    
print("There are %d spaces in the text." % spaces)

