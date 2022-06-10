#!/usr/bin/env python3

# def factorial(n):
#    assert(isinstance(n, int) and n>=0)
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n-1)

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print("enter an integer to take the factorial of!")
print(factorial(int(input())))
