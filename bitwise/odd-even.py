def odd_or_even(n):
    return (n&(n-1)==0)


res = odd_or_even(9)
if(res):
    print('Even')
else:
    print('Odd')

