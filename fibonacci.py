n = int(input("Enter the number of terms: "))

# First two terms
a=0
b=1
if (n==0):
  print("Empty series!")
else:
  print("Fibonacci Series:")
  for i in range(n):
    print(a,end=' ')
    temp=a+b
    a=b
    b=temp
