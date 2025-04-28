# Predict
"""
The value returned is 9
The data type returned is a float
"""

# Modify 1
def add(a: float, b: float) -> float:
   sum = a + b
   return sum

sum = add(7.0, 2.0)
print(sum)

# The data type sum is a float 
# When doing sum = add("book", "keeper"), the datatype sum would be a string

def add(a: float, b: float) -> float:
   sum = a + b
   return sum

sum = add(7.0, 2.0)
print(sum)

if isinstance(sum, float):
  print("True")
else:
  print("False")

# Modify 2

def absolute(n):
   if n < 0:
      return n* -1
   else:
      return n

print(absolute(-100))
print(absolute(-100))

