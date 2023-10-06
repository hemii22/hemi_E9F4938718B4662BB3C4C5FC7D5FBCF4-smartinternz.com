#Implement a recursive function to calculate the factorial of a given number.

def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)

n = int(input("Enter the n(Number): "))
result = factorial(n)
print("The factorial of {} is {}".format(n,result))
