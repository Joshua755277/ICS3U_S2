import math

print("%3s|%5s|%7s|%5s" % ("N", "SQR", "Cubes", "Roots"))
print("---+-----+-------+-----")
for n in range (10, 200, 15):
  sqr = n**2
  cubes = n**3
  root = round(math.sqrt(n), 2)
  print("%3s|%5s|%7s|%5.2f" % (n, sqr, cubes, root))
