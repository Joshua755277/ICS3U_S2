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

b = -12
a = abs(b)
print("The absolute value of %d is %d" % (b, a))
