def factorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * factorial(n - 1)
n=5
print("the number:",n)
print("factorial :",factorial(n))
