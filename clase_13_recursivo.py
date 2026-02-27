#for i in range(5):
#   print(i)

# ejemplo 1:
def countdown(n):
    if n <= 0:
        print("Donel")
    else:
        print(n)
        countdown(n-1)
countdown(10)

# ejemplo 2: factoria de un número
def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
# 5 * 4 * 3 * 2 *1

def fibonacci (n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci (n-2)

print(fibonacci(7))