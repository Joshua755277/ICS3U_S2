# Make
def factorize(n):
  array = []
  for i in range (1, n):
    if n % i == 0:
      array.append(i)
  return array
  
print(factorize(50))

# Make More

n = int(input("Please enter a number: "))

def factorize(n):
  array = []
  for i in range (1, n):
    if n % i == 0:
      array.append(i)
  return array

array = factorize(n)

def total(n):
  sum = 0
  for i in array:
    sum += i
  return sum

print("Factor sum:", total(array))

if (total(array) == n):
  print(n, "is perfect")
elif (total(array) > n):
  print(n, "is abundant")
else:
  print(n, "is deficient")
