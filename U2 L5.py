S = "#"
for i in range(1, 11):
    print(S * i)

# Predict
# It would output:
"""
#
##
###
####
#####
######
#######
########
#########
##########
"""

# Modify 1
for i in range (10, 0, -1):
  print("#" * i)

# Modify 2

spaces = 4
for i in range (1, 10, 2):
  print(" " * spaces, "#" * i)
  spaces -= 1

# Modify 3

spaces = 5
for i in range (1, 13, 2):
  print(" " * spaces, "#" * i)
  spaces -= 1
  
spaces = 1
for i in range (9, 0, -2):
  print(" " * spaces, "#" * i)
  spaces += 1
