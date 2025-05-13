# Predict
# I think the code will output:
# 9
# 8
# 7
# 6
# 5
# 4 
# 3 
# 2
# 1

# My prediction was correct

# Modify 1

count = 9
while (count != 0):
    count -= 1
    print(count)

# The output is different and it will start from 8 to 0 instead of 9 to 1

# Part B

counter = 1
while (counter <= 6):
    row = 1
    triangle_total = 0
    while (row <= counter):
        triangle_total += row
        row += 1
    counter += 1
    
    suffex = "th"
    if (counter == 1):
      suffex = "st"
    elif (counter == 2):
      suffex = "nd"
    elif (counter == 3):
      suffex = "rd"
    print("The %d%s triangular is %d" % (counter, suffex, triangle_total))
    
    















