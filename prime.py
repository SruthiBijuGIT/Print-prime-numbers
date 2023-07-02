# Write a Python program to read the marks in five subjetcs (maximum mark 20 for each subject) and compute the percentage and grade 
# Grade A >=90%
# Grade B >=80%
# Grade C >=70% 
# Grade D >= 60%
# Grade E <60%
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
t = (a+b+c+d+e)/100 *100
m = int(t)
s = str(m)
if m >= 90:
  print(s+'%')
  print("A")
elif m >= 80:
  print(s+'%')
  print("B")
elif m >= 70:
  print(s+'%')
  print("C")
elif m >= 60:
  print(s+'%')
  print("D")
else:
  print(s+'%')
  print("E")


  


