#factorial of a number

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)


res = factorial(1)
print(res)

#Nth fibonacci number

def fibonacci(number):
    if number == 0:
        return 0;
    if number == 1:
        return 1;
    return fibonacci(number-1) + fibonacci(number-2)

res = fibonacci(4)
print(res)