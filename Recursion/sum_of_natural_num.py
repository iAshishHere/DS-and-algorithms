def sum_of_natural_numbers(number):
    if number == 0:
        return 0
    return number + sum_of_natural_numbers(number-1)

print(sum_of_natural_numbers(100))



#same example using tail recursion, initially sum = 0

def sum_of_natural_numbers(number, sum):
    if number == 0:
        return sum
    return sum_of_natural_numbers(number-1, sum+number)

print(sum_of_natural_numbers(100,0))