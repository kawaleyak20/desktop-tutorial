n = int(input("Enter the number of terms: "))

# First two terms
a=0
b=1
if (n==0):
  print("Empty series!")
else:
  print("Fibonacci Series:")
  for i in range(n):
    print (a,end=' ')
    a=b
    b=a+b
