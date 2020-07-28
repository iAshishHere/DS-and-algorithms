def sum_of_digit(num):
    if num == 0:
        return 0
    return (num % 10) + sum_of_digit(num//10)


res = sum_of_digit(101010)
print(res)