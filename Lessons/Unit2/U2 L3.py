# Part A

# 1 

n = int(input("Please enter a number: "))
count = n
fac = 1

while count > 0:
  
    fac *= count
    count -= 1
    
print(n, "factorial is equal to", fac)

# 2

n = int(input("Please enter a number: "))
count = n

print(n, "factorial is equal to ", end="")

while count > 0:
  if count == 1:
    print("1")
    quit()
  print(count, "x", end=" ")
  count -= 1

# 3

n = int(input("Please enter a number: "))
count = n
fac = 1

while count > 0:
  
    fac *= count
    count -= 1
    
print(n, "factorial is equal to", fac)

