# Predict
"""
Predict A:
The purpose is for each word/string in the list, it will append/add the length of each string into the list called sizes
The list items contains string types but the list sizes will contain int types
There will not be any output in this for loop

Predict B:
6 Apples
7 Bananas
8 Cherries
4 Dosa
"""

# Modify 

items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []
for i in range(len(items)): 

    sizeI = len(items[i])
    sizes.append(sizeI)

for i in range(len(sizes)):
  print("%d %s" % (sizes[i], items[i]), end=": ")
  if sizes[i] == len(items[i]):
    print("True")
  else:
    print("False")
  
