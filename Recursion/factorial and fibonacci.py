def factorial(number):
    if number == 1 | number == 0:
        return 1
    return number * factorial(number-1)


#res = factorial(0)
#print(res)

def fibonacci(number):
    if number == 0:
        return 0;
    if number == 1:
        return 1;
    return fibonacci(number-1) + fibonacci(number-2)

res = fibonacci(4)
print(res)