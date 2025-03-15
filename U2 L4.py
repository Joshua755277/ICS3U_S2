n = int(input("Give me a value of n: "))
print("Counting from j = 1 to %d: " % n)
print("%0s %5s %11s" % ("j", "tri", "factorial"))
j = 0
tri = 0
fac = 1
while j < n:
  j += 1
  tri += j
  fac *= j
  print("%d %5d %5d" % (j, tri, fac))
