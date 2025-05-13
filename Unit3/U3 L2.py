# Prediction A:
# It will print out each item in the list, in this case it would look like: ['Apples', 'Bananas', 'Cherries', 'Dosa']

# Predict B:
# It would print out: The number of items is 4.

# Predict C:
"""
Apples
Bananas
Cherries
Dosa

Predict D:
0 Apples
1 Bananas
2 Cherries
3 Dosa
"""

# Modify 
item_num = int(input("How many items are you entering? "))
item_list = []
print("Enter your items now:")
i = 0
while i < item_num:
  next_item = input("Next item:")
  i += 1
  item_list.append(next_item)
print("You have entered %d items." % i)

for x in item_list:
  print(x)
