# Write a Python program to print the prime numbers for a user provided range
x = int(input())
y = int(input())
for i in range(x,y+1):
  if i > 1:
    for j in range(2,i):
      if (i%j) == 0:
        break
    else:
      print(i)
